#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SIZE 1101

struct cifra
{
    char input[MAX_SIZE];

    struct cifra *next;
};

//Cria espaço na memória para receber o input
struct cifra *new_cifra( void )
{
    struct cifra *atual = malloc( sizeof(struct cifra) );

    return atual;

}


void add( struct cifra *head, char *codigo )
{
    struct cifra *atual = head;

    while( atual->next != NULL )
    {
        atual = atual->next;

    }
    
    struct cifra *new = new_cifra();

    strcpy( new->input, codigo);
    atual->next = new;

}


int testa_intervalo(int inicio, int fim, struct cifra *atual )
{
	int last_duplicada = fim;
	
	//Avalia o intervalo, fixando a posição de uma letra e percorrendo as restantes
	for(int i = inicio; i < last_duplicada-1; ++i)
	{
		for (int j = i+1 ; j < last_duplicada; ++j)
		{
			//Se encontrar um par de letras com posições consecutivas
			if (atual->input[i] == atual->input[i+1])
			{
				return i+1;

			}

			//Se encontrar um par de letras em posições não consecutivas
			else if (atual->input[i] == atual->input[j])
			{
				//Guarda a posição da última peça duplicada 
				last_duplicada = j;
			}
		}
	}

	//Devolve a posição da peça duplicada no array
	return last_duplicada;
}


void descodificar( struct cifra *atual )
{	
	int inicio = 0, fim = 1;
	int tamanho_input = strlen(atual->input);
	
	
	while(inicio < tamanho_input-1 && fim < tamanho_input)
	{
		int avancar; 

		//Quando encontra um par de letras duplicado
		if(atual->input[inicio] == atual->input[fim])
		{
				
			//Se o par estiver em posições consecutivas
			if (fim == inicio + 1)
			{
				printf("%c", atual->input[fim]);
				inicio = fim + 1;

			}
			else
			{
				avancar = testa_intervalo(inicio+1, fim, atual);
				printf("%c", atual->input[avancar]);
				inicio= avancar+1;

			}

			//Depois de atualizado o inicio, o fim assume a posição seguinte
			fim = inicio + 1;

		}
		//Quando chega ao final do array
		else if(fim == tamanho_input-1)
		{
			inicio++;
			fim = inicio + 1;

		}
		else
			fim++;

	}
	printf("\n");

}


int main()
{
	char codigo[MAX_SIZE];

	struct cifra* head = new_cifra();

	while(scanf("%s", codigo) != EOF)
	{
		add(head, codigo);
		
	}

	struct cifra *atual = head;

    while( atual->next != NULL )
    {
        atual = atual->next;
        descodificar(atual);
      
    }

    return 0;

}