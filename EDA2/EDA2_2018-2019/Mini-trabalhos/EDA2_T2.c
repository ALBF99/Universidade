#include <stdio.h>


int jogo_A(int inicio, int fim, int sz, int v[sz])
{
	return v[inicio] > v[fim] ? inicio : fim;
	
}


int jogo_B(int modo, int inicio, int fim, int sz, int v[sz])
{
	if(modo == 1)
		return v[inicio] < v[fim] ? inicio : fim;

	else
		return jogo_A(inicio, fim, sz, v);

}


void jogo(int sz, int v[sz])
{
	int pontos_A = 0;
	int pontos_B = 0;
	int inicio = 0;
	int fim = sz-1;
	int modo = 1;
	int posicao;
	int posicao_intermedia;
	

	for(int i = 1; i <= sz; i++)
	{	
		posicao_intermedia = (inicio+fim)/2;
		
		if(i%2 != 0)
		{
			posicao = jogo_A(inicio, fim, sz, v);
			pontos_A += v[posicao];

		}
		else
		{
			posicao = jogo_B(modo, inicio, fim, sz, v);
			pontos_B += v[posicao];
			modo = modo * -1;
			
		}


		if(posicao > posicao_intermedia)
			fim--;
		else
			inicio++;

	}


	if(pontos_A > pontos_B)

		printf("Alex ganha com %d contra %d\n", pontos_A, pontos_B);
	
	else if (pontos_A == pontos_B)
	
		printf("Alex e Bela empatam a %d\n", pontos_A);
	
	else
	
		printf("Bela ganha com %d contra %d\n", pontos_B, pontos_A);
	
	
}


int main(void)
{
	int n_montes;
	
	scanf("%d", &n_montes);
		
	
	int sequencia[n_montes-1];

	for(int i = 0; i < n_montes; i++)
	{	
		scanf("%d", &sequencia[i]);

	}

	jogo(n_montes, sequencia);

	return 0;

}