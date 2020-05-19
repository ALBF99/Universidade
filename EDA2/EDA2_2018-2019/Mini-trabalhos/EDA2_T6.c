#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LIGACOES 1000


struct node
{
    int num_sensor;
    struct node *next;

};


struct node *sensor_construtor( void )
{
    struct node *aux = ( struct node* )malloc( sizeof(struct node) );

    return aux;

}


/*
	Adiciona uma ligação a um sensor, á qual este passa a poder enviar mensagem
	Dada a referência da lista (apontador para um certo índice do array de sensores),
	adiciona um novo sensor no final da lista

	sensor_recetor - sensor que queremos adicionar
*/
void adicionar_sensor( struct  node **array_sensores, int sensor_emissor, int sensor_recetor)
{
	struct node *ligacao_sensor;
	struct node *lista = array_sensores[sensor_emissor];

	//Criação do novo nó que contém a nova ligação
	ligacao_sensor = sensor_construtor();
	ligacao_sensor->num_sensor = sensor_recetor;
	ligacao_sensor->next = NULL;

    //Enquando não chegar ao final da lista passa ao seguinte nó
	while(lista->next != NULL)
	{
		lista = lista->next;

	}

		lista->next = ligacao_sensor;

}


/*
	Apaga uma ligação de um sensor emissor, passando a não poder enviar mensagem
	Dada a referência da lista (apontador para um certo índice do array de sensores),
	apaga um sensor da lista

	sensor_recetor - sensor que queremos eliminiar
*/
void apagar_sensor (struct  node **array_sensores, int sensor_emissor, int sensor_recetor)
{
	struct node *lista = array_sensores[sensor_emissor];

	//Apontador para o nó anterior
	struct node *anterior;

	/*
		Enquanto não se encontra o sensor que queremos eliminar,
		guardamos a posição do nó anterior
	*/
	while( lista->num_sensor != sensor_recetor)
	{
		anterior = lista;
		lista = lista->next;

	}
	/*
		Rearranjo de ligações entre nós.
		As ligações com o nó eliminado são cortadas, 
		o nó anterior ao eliminado e o seu nó seguinte passam a estar ligados
	*/ 
	anterior->next = lista->next; 

}


/*
	Avalia se uma mensagem pode ser enviada de um sensor para outro
	Se for verdade, retorna 1. Senão retorna 0

	Dada a referência da lista (apontador para um certo índice do array de sensores),
	procura se o valor do sensor_recetor está contido nessa mesma lista

	sensor_recetor - sensor que recebe a mensagem
*/
int procurar_caminho(struct  node **array_sensores, int sensor_emissor, int sensor_recetor)
{
	struct node *lista = array_sensores[sensor_emissor];

	//Enquanto não se encontrar o sensor passa ao segiunte (dentro dos limites da lista)
	while( lista != NULL && lista->num_sensor != sensor_recetor )
	{
		lista = lista->next;

	}

	if( lista != NULL && lista->num_sensor == sensor_recetor )
		return 1;
	
	return 0;	

}


int main(void)
{
	int n_sensores, sensor_emissor, sensor_recetor, n_sensores_caminho, valido;
	char operador;
	int caminho[MAX_LIGACOES];

	scanf("%d", &n_sensores);
	
	/*
		Array de linkedLists
		Cada índice corresponde a um sensor, por exemplo, ao índice 0 corresponde o sensor 0
		Nele é guardado todos os sensores a que um certo sensor pode enviar mensagem
	*/
	struct node* array_sensores[n_sensores];
	
	/*
		Criação do primeiro nó para cada sensor
		Mete esse nó a valer -1, simbolizando que ainda nao tem nenhuma ligação a outro sensor
	*/
	for(int i=0; i < n_sensores; i++)
	{
		array_sensores[i] = sensor_construtor();
		array_sensores[i]->num_sensor = -1;
	
	}

	while(scanf("%c", &operador) != EOF)
	{
		
		switch(operador)
		{
			case '+':
				scanf("%d %d\n", &sensor_emissor, &sensor_recetor);
				adicionar_sensor(array_sensores, sensor_emissor, sensor_recetor);
				break;


			case '-':
				scanf("%d %d\n", &sensor_emissor, &sensor_recetor);
				apagar_sensor(array_sensores, sensor_emissor, sensor_recetor);
				break;


			case '?':
				scanf("%d", &n_sensores_caminho);
				
				// Guarda as ligações que queremos testar num array
				for(int i = 0; i <= n_sensores_caminho; i++)
				{
					scanf("%d", &caminho[i]);
					
				}

				for(int i = 0; i < n_sensores_caminho; i++)
				{
					valido = procurar_caminho(array_sensores, caminho[i], caminho[i+1]);
					
					/*
						Se não for possível enviar mensagem de sensor x para sensor x+1.
						Imprime a mensagem e sai do ciclo for, pois não necessita de testar 
						para os sensores seguintes
					*/
					if( !valido )
					{
						printf("no [%d..%d]\n", caminho[0], caminho[n_sensores_caminho]);
						break;

					}
				}
				
				//Se for possivel enviar mensagem desde o primeiro ao último, imprime a mensagem
				if( valido ) 
				{
					printf("yes [%d..%d]\n", caminho[0], caminho[n_sensores_caminho]);
				}
				
				break;


			default:
				continue;

		}
	}

	return 0;

}