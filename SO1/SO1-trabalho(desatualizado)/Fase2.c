#define _XOPEN_SOURCE 700 
#include <stdlib.h> 
#include <stdio.h> 
#include <string.h>
#include "header.h"

#define NEW 1
#define READY 2
#define RUN 3
#define BLOCK 4
#define EXIT 5

#define QUANTUM 4
#define TEMP_BLOCK 3
#define MEM_SIZE 300

/*
Array onde está guardada as variáveis e as instruções 
indice 0-9: variáveis globais??
*/
int MEM[MEM_SIZE];
struct pcb *lista_processos;
char *aux_ficheiro[20];
int n_processos;
//Queue para cada estado 
struct Queue *queueNew; 
struct Queue *queueReady;
struct Queue *queueRun; 
struct Queue *queueBlock; 
struct Queue *queueExit;  


int add_inst( int i, int inst, int v1, int v2)
{
	MEM[i] = inst;
	MEM[i+1] = v1;
	MEM[i+2] = v2;

	return i+3;

}

void add_pcb(struct pcb *p, int i, int t, int idx)
{	
	p[i].pid = i+1;
	p[i].pc = &MEM[idx+3];
	p[i].estado = 0;
	p[i].localizador_instrucoes = &MEM[idx];
	p[i].tempo = t;

	p[i].tempoBlock = -1;
	p[i].tempoRun = -1;
	p[i].tempoNew = -1;
	p[i].tempoExit = -1;

}


void start_queues()
{
	queueNew = createQueue(); 
	queueReady = createQueue();
	queueRun = createQueue(); 
	queueBlock = createQueue(); 
	queueExit = createQueue();  


}


int check_time(int i)
{
	return lista_processos[i].tempo;

}

int check_status(int i)
{
	return lista_processos[i].estado;

}

int check_timeLeftRun(int i)
{
	return lista_processos[i].tempoRun;

}

int check_timeLeftBlock(int i)
{
	return lista_processos[i].tempoBlock;

}

void update_tempo(int i, int val)
{
	val++;
	lista_processos[i].tempo = val;
}


void update_status(int i, int new_estado)
{
	lista_processos[i].estado = new_estado;

}

void update_tempoRun(int i, int val)
{
	val--;
	lista_processos[i].tempoRun = val;

}

void update_tempoBlock(int i, int val)
{
	val--;
	lista_processos[i].tempoBlock = val;

}

void avancar_inst(int i)
{
	int *ptr = lista_processos[i].localizador_instrucoes;
	ptr = lista_processos[i].pc;
	lista_processos[i].pc = ptr + 3;

}

void check_prioridade()
{
	int aux; 
/*
	if (queueBlock->front != NULL)
	{
		printf("oihfdbjdh\n");
		if(queueBlock->front->processo->tempoBlock == 0)
		{
			aux = queueBlock->front->processo->pid;
			blockToReady(aux-1);
			update_status(aux-1, READY);
			printf("%d\n", queueBlock->front->processo->tempoBlock );

		}
		
	}
*/
	if(queueRun->front != NULL)
	{
		if(queueRun->front->processo->tempoRun == 0)
		{
			aux = queueRun->front->processo->pid;
			runToReady(aux-1);
			update_status(aux-1, READY);
		}
		
	}

	if(queueNew->front != NULL)	{
		if(queueNew->front->processo->tempoNew == 1)
		{
			aux = queueNew->front->processo->pid;
			newToReady(aux-1);
			update_status(aux-1, READY);

		}
	}

}

int estados()
{
	int ciclo = 0, aux_ciclo = 0, num_processo = 0, est, flag_run = 0, flag_block = 0, flag_new = 0, instrucao, aux_time, n_exit;


	while(1)
	{
		printf("Ciclo:%d\n", ciclo );
		printf("Processo:%d\n", num_processo );
		printf("Estado:%d\n", check_status(num_processo));

		if(check_time(num_processo) == ciclo)	
		{
			lista_processos[num_processo].estado = 1;
		}

		switch(check_status(num_processo))
		{
			case NEW:
				if(lista_processos[num_processo].tempoNew == 1)
				{
					if(queueReady->front == NULL)
					{
						newToReady();
						readyToRun();
						update_status(num_processo, RUN);
						update_tempoRun(num_processo, QUANTUM);
						break;
					}
					break;
				}
				else
				{
					printf("CONA\n");
					entraNew(num_processo);
					update_status(num_processo, NEW);
					lista_processos[num_processo].tempoNew++;
					break;
				}
				break;

			case READY:
				//Se não estiver nenhum processo no Run
				if(queueRun->front == NULL)
				{
					readyToRun();
					update_status(num_processo, RUN);
					update_tempoRun(num_processo, QUANTUM);
					break;

				}
				
				break;

			case RUN:

				/*
				Times up!
				-> Se o Ready está vazio continua a correr
				-> Se não estiver vazio vai para o Ready
				*/
				printf("TEMPO RUN %d\n", check_timeLeftRun(num_processo));
				if(check_timeLeftRun(num_processo) == 0)
				{
					//check_prioridade();
					if(queueReady->front == NULL && queueNew->front->processo->tempoNew != 1 && queueBlock->front->processo->tempoBlock != 0)
					{

						update_tempoRun(num_processo, QUANTUM);
						break;
					}

					break;
				}
				else{

					instrucao = *lista_processos[num_processo].localizador_instrucoes;
					avancar_inst(num_processo);

					if(instrucao == 1)
					{
						aux_time = check_timeLeftRun(num_processo);
						update_tempoRun(num_processo, aux_time);
						break;

					}
					else if(instrucao == 8)
					{
						runToBlock();
						update_tempoRun(num_processo, 0);
						update_status(num_processo, BLOCK);
						update_tempoBlock(num_processo, TEMP_BLOCK);
						break;

					}
					else if(instrucao == 11)
					{
						runToExit();
						update_tempoRun(num_processo, 0);
						update_status(num_processo, EXIT);
						break;
					}
					break;

				}
			case BLOCK:

				if(check_timeLeftBlock(num_processo) == 0)
				{
					
					blockToReady();
					update_status(num_processo, READY);
					break;

				}
				aux_time = check_timeLeftBlock(num_processo);
				update_tempoBlock(num_processo,aux_time);
				break;

			case EXIT:
				if(lista_processos[num_processo].tempoExit == 0)
				{
			
					lista_processos[num_processo].tempoExit ++;
				}
				else
				{
					saidaExit();
				}
				break;
		
			default:
				break;


		}
		

		if(lista_processos[num_processo].estado == EXIT)
		{
			n_exit++;

			if(n_exit == n_processos)
			{
				return 0;
			}
		}



		if(num_processo == n_processos-1)
		{
			num_processo = 0;
			check_prioridade();
			printf("%d |P1 %d|P2 %d|P3 %d\n", ciclo, lista_processos[0].estado, lista_processos[1].estado, lista_processos[2].estado );
			ciclo++;
			n_exit = 0;
			
			
		}
		else
			num_processo++;

/*
		if(lista_processos[0].estado == EXIT && lista_processos[1].estado == EXIT && lista_processos[2].estado == EXIT)
		{
			return 0;
		}

*/	
	}

}

/*
void entraNew( int i)
{
	struct QNode *node = new_node(&lista_processos[i]);
	enQueue(queueNew, node);

}
*/
void entraNew( int t)
{	
	for(int i = 0; i < n_processos; i++)
	{
		if(lista_processos[i].tempo == t)
		{
			struct QNode *node = new_node(&lista_processos[i]);
			enQueue(queueNew, node);
			update_status(i, NEW);
			lista_processos[i].tempoNew++;

		}
	}
}
/*
void newToReady()
{
	struct QNode *ptr = deQueue(queueNew);
	enQueue(queueReady, ptr);

}
*/
void newToReady()
{
	for (int i = 0; i < n_processos; ++i)
	{
		if(lista_processos[i].tempoNew == 1)
		{
			struct QNode *ptr = deQueue(queueNew);
			enQueue(queueReady, ptr);
			update_status(i, READY);
			update_tempoRun(i, QUANTUM);
		}
	}

}

/*
void readyToRun()
{
	struct QNode *ptr = deQueue(queueReady);
	enQueue(queueRun, ptr);

}
*/
void readyToRun()
{
	int aux;
	aux = queueReady->front->processo->pid;

	if(queueRun->front == NULL)
	{
		struct QNode *ptr = deQueue(queueReady);
		enQueue(queueRun, ptr);
		update_status(aux, RUN);
		update_tempoRun(aux, QUANTUM);

	}
}
/*
void runToReady()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueReady, ptr);

}
*/
void runToReady()
{
	int aux, aux_time, instrucao; 

	if(queueRun->front != NULL)
	{
		aux = queueRun->front->processo->pid;

		if(check_timeLeftRun(aux) == 0)
		{
			struct QNode *ptr = deQueue(queueRun);
			enQueue(queueReady, ptr);
			update_status(aux-1, READY);
		}
		else if(check_timeLeftRun(aux) != -1)
		{
			
			instrucao = *lista_processos[aux].localizador_instrucoes;
			avancar_inst(aux);

			if(instrucao == 1)
			{
				struct QNode *ptr = deQueue(queueRun);
				enQueue(queueExit, ptr);
				update_tempoRun(aux, 0);
				update_status(aux, EXIT);
			}
		}
	}

}
/*
void runToExit()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueExit, ptr);
}
*/
void runToExit()
{
	int aux, instrucao;
	aux = queueRun->front->processo->pid;
	instrucao = *lista_processos[aux].localizador_instrucoes;
	avancar_inst(aux);

	if(instrucao == 11)
	{
		struct QNode *ptr = deQueue(queueRun);
		enQueue(queueExit, ptr);
		update_tempoRun(aux, 0);
		update_status(aux, EXIT);
	}
}
/*
void runToBlock()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueBlock, ptr);

}
*/
void runToBlock()
{
	int aux, instrucao;
	aux = queueRun->front->processo->pid;
	instrucao = *lista_processos[aux].localizador_instrucoes;
	avancar_inst(aux);

	if(instrucao == 11)
	{
		struct QNode *ptr = deQueue(queueRun);
		enQueue(queueBlock, ptr);
		update_tempoRun(aux, 0);
		update_status(aux, EXIT);
	}

}
	
/*
void blockToReady()
{
	struct QNode *ptr = deQueue(queueBlock);
	enQueue(queueReady, ptr);
}
*/
void blockToReady()
{
	int aux, aux_time; 

	if(queueBlock->front != NULL)
	{
		aux = queueBlock->front->processo->pid;

		if(check_timeLeftBlock(aux) == 0)
		{
						
			struct QNode *ptr = deQueue(queueBlock);
			enQueue(queueReady, ptr);
			update_status(aux-1, READY);

		}
		else if(check_timeLeftBlock(aux) != -1)
		{
			aux_time = check_timeLeftBlock(aux);
			update_tempoBlock(aux,aux_time);

		}
	}
	
	
}


int  saidaExit()
{
	int aux, flag = 0;
	aux = queueExit->front->processo->pid;

	for(int i=0; i< n_processos; i++)
	{
		if(lista_processos[i].tempoExit == 0)
		{
			
			lista_processos[i].tempoExit ++;
		}
		else if(lista_processos[i].tempoExit == 1)
		{
			deQueue(queueExit);
			update_status(i, -1);
			lista_processos[i].tempoExit= -1;
			flag++;
		}

	}

	return flag;
	
	
	
}

void modelo()
{
	int n = 0;
	int t = 0;

	while(n != n_processos)
	{
		blockToReady();
		runToReady();
		newToReady();
		entraNew(t);
		readyToRun();
		runToBlock();
		runToExit();
		n = saidaExit();
		printf("%d |P1 %d|P2 %d|P3 %d\n", t, lista_processos[0].estado, lista_processos[1].estado, lista_processos[2].estado );
		t++;
	}

}

void read_ficheiro()
{
	FILE *ptrToFile;
	char* linha = NULL;
	size_t len = 0;
	size_t read;
	
	int tamanho, time_start, inst, v1, v2;

	ptrToFile = fopen ("input1.txt", "r");

	if(ptrToFile == NULL)
	{
		printf("Ficheiro não encontrado!");
	}
	else
	{

		while ((read = getline(&linha, &len, ptrToFile))!= -1)
		{
			
			aux_ficheiro[n_processos] = strdup(linha);
			printf("%s\n", aux_ficheiro[n_processos] );
			
			//Fico a saber quantos processos são
			n_processos++;

		}
		printf("%d\n", n_processos);
		fclose(ptrToFile);

		/*
			Criar espaço 
			lista_processos -> array de structs onde se guarda o pcb
		*/
		lista_processos = (struct pcb*) malloc(n_processos * sizeof( struct pcb));

		int index_mem = 10;

		for (int i = 0; i < n_processos; i++)
		{
			time_start = atoi(&aux_ficheiro[i][0]);

			add_pcb(lista_processos, i, time_start, index_mem);

			tamanho = strlen(aux_ficheiro[i]);

			//Passar as instruções para a MEM
			for(int j = 2; j < tamanho-1; j = j+6)
			{
					
				inst = atoi(&aux_ficheiro[i][j]);
				v1 = atoi(&aux_ficheiro[i][j+2]);
				v2 = atoi(&aux_ficheiro[i][j+4]);

				index_mem = add_inst(index_mem, inst, v1, v2);

					
			}

			//Mostra que está a apontar para a primeira instrução de cada processo
			printf("Processo: %d\nPrimeira instrução:%d Next: %d\n ", lista_processos[i].pid, *lista_processos[i].localizador_instrucoes, *lista_processos[i].pc);
			printf("Tempo chegada: %d\n", lista_processos[i].tempo);
			printf("TIME:%d\n", check_time(i));
		}
		/*
		Número de instruções no total + 10 das variáveis
		*/
		//printf("%d\n", index_mem );

		//Testa se as instruções estão a ser bem guardadas
		for(int k = 10; k < index_mem; k=k+3 )
		{
			printf("%d %d %d\n", MEM[k], MEM[k+1], MEM[k+2] );
		}

	}
}

int main(void)
{
	read_ficheiro();
	start_queues();

	//estados();
	modelo();

	return 0;
	
}
