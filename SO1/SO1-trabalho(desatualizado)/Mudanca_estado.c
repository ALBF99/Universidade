#include <stdlib.h> 
#include <stdio.h> 
#include <string.h>
#include "header.h"

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

struct QNode* new_node(struct pcb *k)
{ 
    struct QNode *temp = (struct QNode*)malloc(sizeof(struct QNode)); 
    temp->processo = k; 
    temp->next = NULL; 

    return temp;
}
/*
void entraNew( int i)
{
	struct QNode *node = new_node(&lista_processos[i]);
	enQueue(queueNew, node);

}
*/
/*
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
*/
/*
void newToReady()
{
	struct QNode *ptr = deQueue(queueNew);
	enQueue(queueReady, ptr);

}
*/
/*
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
*/
/*
void readyToRun()
{
	struct QNode *ptr = deQueue(queueReady);
	enQueue(queueRun, ptr);

}
*/
/*
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
*/
/*
void runToReady()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueReady, ptr);

}
*/
/*
void runToReady()
{
	int aux, aux_time, instrucao; 
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
*/
/*
void runToExit()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueExit, ptr);
}
*/
/*
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
*/
/*
void runToBlock()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueBlock, ptr);

}
*/
/*
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
/*
void blockToReady()
{
	int aux, aux_time; 
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

*/
/*
int  saidaExit()
{
	int aux, flag = 0;
	aux = queueExit->front->processo->pid;

	for(int i=0, i< n_processos, i++)
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
*/