#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define PONTOS 0
#define VITORIAS 1
#define EMPATES 2
#define DERROTAS 3
#define MARCADOS 4
#define SOFRIDOS 5

#define EQUIPA_1 0
#define GOLOS_1 1
#define EQUIPA_2 2
#define GOLOS_2 3


void pontuacao(int idx_equipa1, int idx_equipa2, int n_jogo, int num_jogos, char jogos[num_jogos][4][21], int num_equipas, int info_equipas[num_equipas][6])
{
	int golos_equipa1 = atoi(jogos[n_jogo][GOLOS_1]);
	int golos_equipa2 = atoi(jogos[n_jogo][GOLOS_2]);

	
	info_equipas[idx_equipa1][MARCADOS] += golos_equipa1;
	info_equipas[idx_equipa2][MARCADOS] += golos_equipa2;
	info_equipas[idx_equipa1][SOFRIDOS] += golos_equipa2;
	info_equipas[idx_equipa2][SOFRIDOS] += golos_equipa1;
	

	if(golos_equipa1 > golos_equipa2)
	{
		info_equipas[idx_equipa1][PONTOS] += 3;
		info_equipas[idx_equipa1][VITORIAS] += 1;
		info_equipas[idx_equipa2][DERROTAS] += 1;

	}	
	else if(golos_equipa1 < golos_equipa2)
	{
		info_equipas[idx_equipa2][PONTOS] += 3;
		info_equipas[idx_equipa2][VITORIAS] += 1;
		info_equipas[idx_equipa1][DERROTAS] += 1;

	}
	else
	{
		info_equipas[idx_equipa1][PONTOS] += 1;
		info_equipas[idx_equipa2][PONTOS] += 1;
		info_equipas[idx_equipa1][EMPATES] += 1;
		info_equipas[idx_equipa2][EMPATES] += 1;

	}
}


void resultados(int num_jogos, char jogos[num_jogos][4][21], int num_equipas, char nome_equipas[num_equipas][21], int info_equipas[num_equipas][6])
{

	for(int i = 0; i < num_jogos; ++i)
	{
		for(int j = 0; j < num_equipas; ++j)
		{
			for(int k = 0; k < num_equipas; ++k)
			{
				if(strcmp(jogos[i][EQUIPA_1], nome_equipas[j]) == 0 && strcmp(jogos[i][EQUIPA_2], nome_equipas[k]) == 0)
				{
					pontuacao(j, k, i, num_jogos, jogos, num_equipas, info_equipas);

				}
			}
		}
	}
}


void display_resultados(int num_equipas, int info_equipas[num_equipas][6], char nome_equipas[num_equipas][21])
{
	int idx_vencedor = 0; 
	int pts_empate, aux_pts = 0;

	for (int i = 0; i < num_equipas; ++i)
	{

		if (aux_pts < info_equipas[i][PONTOS])
		{
			idx_vencedor = i;
			aux_pts = info_equipas[i][PONTOS];

		}
		else if (aux_pts == info_equipas[i][PONTOS])
		{
			pts_empate = aux_pts;
		}
		
	}

	if(pts_empate == aux_pts)
	{
		printf("torneio sem vencedora\n");
	}
	else
	{
		printf("a vencedora foi %s, com %d ponto(s)\n", nome_equipas[idx_vencedor], info_equipas[idx_vencedor][PONTOS]);
		printf("ganhou %d jogo(s), empatou %d jogo(s) e perdeu %d jogo(s)\n", info_equipas[idx_vencedor][VITORIAS], info_equipas[idx_vencedor][EMPATES],
		 info_equipas[idx_vencedor][DERROTAS] );
		printf("marcou %d golo(s) e sofreu %d golo(s)\n", info_equipas[idx_vencedor][MARCADOS], info_equipas[idx_vencedor][SOFRIDOS] );
	}
}

int main(void)
{
	int num_equipas, num_jogos;

	scanf("%d %d", &num_equipas, &num_jogos);


	char nome_equipas[num_equipas][21];
	int info_equipas[num_equipas][6];
	char jogos[num_jogos][4][21];

	memset( info_equipas, 0, num_equipas*6*sizeof(int) );

	for(int i = 0; i < num_equipas; ++i)
	{
		scanf("%s", nome_equipas[i]);

	}

	for (int j = 0; j < num_jogos; ++j)
	{
		scanf("%s %s - %s %s", jogos[j][EQUIPA_1], jogos[j][GOLOS_1], jogos[j][EQUIPA_2], jogos[j][GOLOS_2]);

	}

	
	resultados(num_jogos, jogos, num_equipas, nome_equipas, info_equipas);
	display_resultados(num_equipas, info_equipas, nome_equipas);

	return 0;
}