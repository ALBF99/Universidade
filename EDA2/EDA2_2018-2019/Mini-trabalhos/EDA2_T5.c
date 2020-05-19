#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct route
{
	int rede_abc;
	int interface;

};

void trocar_valores(struct route* array_route, int posicao1, int posicao2)
{
	struct route aux;

	aux = array_route[posicao1];
	array_route[posicao1] = array_route[posicao2];
	array_route[posicao2] = aux;
}

/*
	Implementação do algoritmo de ordenação QuickSort
	Fonte: https://beginnersbook.com/2015/02/quicksort-program-in-c/
*/

void quicksort(struct route* array_route, int first, int last)
{
   int i, j, pivot;

   if(first < last)
   {
      pivot=first;
      i=first;
      j=last;

      while(i<j)
      {
         while(array_route[i].rede_abc <= array_route[pivot].rede_abc && i<last)
            i++;

         while(array_route[j].rede_abc > array_route[pivot].rede_abc)
            j--;

         if(i<j)
            trocar_valores(array_route, i, j);
         
      }

      trocar_valores(array_route, pivot, j);
      quicksort(array_route,first,j-1);
      quicksort(array_route,j+1,last);

   }
}

/*
	Implementação do professor Vasco Pedro
	disponível no slide correspondente à aula teórica nº3 
*/

int pesquisa_dicotomica_recursiva(struct route* array_route, int endereco, int inicio, int fim)
{
	if( inicio > fim)
		return -1;

	int m = (inicio + fim) / 2;

	if (endereco < array_route[m].rede_abc)
		return pesquisa_dicotomica_recursiva(array_route, endereco, inicio, m - 1);

	if (endereco > array_route[m].rede_abc)
		return pesquisa_dicotomica_recursiva(array_route, endereco, m + 1, fim);

	return m;
}


void encaminhamento(struct route* array_route,int n_routes,int endereco)
{
	//Variável que guarda a posição intermédia do array
	int middle = (n_routes-1)/2;
	int default_route_active = -1, match_route = -1;

	/*
		Confirma a existência de uma default route(0.0.0.0)
		Caso exista, após o QuickSort assume sempre a primeira posição do array 

	*/
	if (array_route[0].rede_abc == 0)
		default_route_active *= -1;
	
	/*
		Comparação do endereço com o route que se encontra na posição intermédia
		Assim, dependendo da situação começamos a pesquisa binária à esquerda ou à direita 
		da posição intermédia
	*/
	if(endereco > array_route[middle].rede_abc)

		match_route = pesquisa_dicotomica_recursiva(array_route, endereco, middle + 1, n_routes);

	else if(endereco < array_route[middle].rede_abc)

		match_route = pesquisa_dicotomica_recursiva(array_route, endereco, 0, middle - 1);

	else if(endereco == array_route[middle].rede_abc)

		match_route = middle;


	/*
		Escreve no standard output o número da interface
		a usar para o encaminhamento
	*/
	if (match_route == -1 && default_route_active == -1)
		printf("no route\n");
	
	else if(match_route == -1 && default_route_active == 1)
		printf("%d\n", array_route[0].interface);
	
	else
		printf("%d\n", array_route[match_route].interface);
	


}


int main(void)
{
	int n_routes;
	int endereco;
	int aux_redeA, aux_redeB , aux_redeC, aux_rede;

	scanf("%d\n", &n_routes);

	struct route *array_route = ( struct route* ) malloc(n_routes * sizeof( struct route));

	for(int i = 0; i < n_routes; i++)
	{
		scanf("%d.%d.%d.0 %d", &aux_redeA, &aux_redeB, &aux_redeC, &array_route[i].interface );

		//Converter o formato a.b.c em um só número
		aux_rede = aux_redeA * pow(10, 6) + aux_redeB * pow(10, 3) + aux_redeC;
		array_route[i].rede_abc = aux_rede;

	}

	quicksort(array_route,0, n_routes-1);


	while(scanf("%d.%d.%d.%d ", &aux_redeA, &aux_redeB, &aux_redeC, &aux_rede) != EOF)
	{
		//Converter o formato a.b.c em um só número
		aux_rede = aux_redeA * pow(10, 6) + aux_redeB * pow(10, 3) + aux_redeC;
		endereco = aux_rede;

		encaminhamento(array_route, n_routes, endereco);	
	}

    return 0;
}
