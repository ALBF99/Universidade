#include <stdio.h>
#include <string.h>
#include "colorSquare.h"

void iterativo(){
    int sz= 0;
    while (sz<2 || sz>20){
        printf("\nTamanho do tabuleiro:");
        scanf("%d", &sz);
        if (sz<2 || sz>20){
            printf("\nTamanho inválido! Introduz novo tamanho\n");
        }
    }


    int num_pecas=sz*sz;
    int total = 0;
    int aux;

    //criação do tabuleiro original
    int tabuleiro[20][20];
    for(int i=0; i<sz; i++){
        for(int j=0; j<sz; j++){
            tabuleiro[i][j]= rand() %4 +1;
        }
    }

    printf("\n");
    mostrar(tabuleiro, sz);

    //Condição de paragem: Para quando não houver mais peças no tabuleiro
    while(num_pecas>0){
        int x, y;
        printf("\nJogada (no formato x y):");
        scanf("%d %d", &x, &y);


        //exemplo: jogada(0,0) corresponde à posição (2,0) numa matriz de 3x3
        // formato da jogada (x, y) -> formato da matriz (y, x)
        // x-> linha ; y-> coluna

        int y_aux=(sz-1)-y;
        int x_real = y_aux;
        int y_real = x;


        if(y_real>=sz||x_real<0 ){
            printf("Jogada Inválida!\n");
        }
        else if(tabuleiro[x_real][y_real]==0){
                printf("Peça já eliminada! Introduz uma nova jogada.\n");
        }
        else if(tabuleiro[x_real][y_real]!=0 && x_real<sz && y_real<sz){
            printf("\nPontuação da jogada:");
            aux = jogada(tabuleiro, sz, x_real, y_real);
            printf("%d \n", aux);
            total = total + aux;
            mostrar(tabuleiro, sz);
            num_pecas = (sz*sz)-contaZeros(tabuleiro, sz);

        }

    }
    printf("Terminou o jogo com uma pontuação total: %d\n", total);
}

