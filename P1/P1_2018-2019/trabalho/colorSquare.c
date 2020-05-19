#include <stdio.h>
#include <string.h>
int total = 0;

//Verifica se o jogo acabou
int contaZeros(int tabuleiro[][20], int sz){
    int conta=0;
    for(int i=0; i<sz; i++){
        for(int j=0; j<sz; j++){
            if (tabuleiro[i][j]==0){
                conta++;
            }
        }
    }

    return conta;
}


void auxMarcar (int tabuleiro[][20], int sz, int x, int y, int num, int tab_aux[][sz]){
    if(tabuleiro[x][y]==num){

        tabuleiro[x][y]=0;
        tab_aux[x][y]=1;
        if(x+1<sz){
            auxMarcar(tabuleiro, sz, x+1, y, num, tab_aux);
        }
        if(y+1<sz){
            auxMarcar(tabuleiro, sz, x, y+1, num, tab_aux);
        }
        if(x-1>=0){
            auxMarcar(tabuleiro, sz, x-1, y, num, tab_aux);
        }
        if(y-1>=0){
            auxMarcar(tabuleiro, sz, x, y-1, num, tab_aux);
        }
    }
}


int marcar (int tabuleiro[][20], int sz, int x, int y){
    int num_quadrados=0;
    int tab_aux[sz][sz];


    //criação de uma matriz com valores 0
    for(int i=0; i<sz;i++){
        for(int j=0; j<sz; j++){
            tab_aux[i][j]=0;
        }
    }

    int num = tabuleiro[x][y];

    auxMarcar(tabuleiro, sz, x, y, num, tab_aux);


    //conta os 1s na tabela auxiliar que representam as peças eliminadas nessa jogada
    for(int i=0; i<sz; i++){
        for(int j=0; j<sz; j++){
            if (tab_aux[i][j]==1){
                num_quadrados++;
            }
        }
    }

    return num_quadrados;
}



int pontuacao(int num_quadrados){
    int pontos;
    pontos = (num_quadrados*(num_quadrados+1))/2;
    return pontos;
}

void gravidade(int tabuleiro[][20], int sz) {
    int k = 0;

    //volta a verificar se a gravidade foi totalmente feita
    while (k < sz) {
        for (int i = 0; i <sz; i++){
            for (int j = 0; j <sz; j++) {
                if (j > 0 && tabuleiro[j][i] == 0) {
                    tabuleiro[j][i] = tabuleiro[j-1][i];
                    tabuleiro[j-1][i] = 0;
                }
            }
        }
        k++;
    }

}


void coluna(int tabuleiro[][20], int sz){
    int k = 0;
    while (k < sz) {
        //fixamos uma coluna e vamos percorrendo as linhas
        for(int j=0; j<sz; j++){

            int coluna_vazia = 0;

            for(int i=0; i<sz; i++){
                if (tabuleiro[i][j] == 0){
                    coluna_vazia+=1;
                }
            }

            //Se o num de 0 for igual ao tamanho do tabuleiro significa que estamos na presença de uma coluna vazia
            if(coluna_vazia == sz){

                //fixamos a linha e vamos percorrendo as coluna
                //quando acabada uma linha passamos para a próxima
                for (int i = 0; i<sz; i++){

                    int j_aux = j;
                    int tab_aux = tabuleiro[i][j_aux];

                    //Puxa para a esquerda os valores
                    // EX: - 1 2 1 -> 1 - 2 1 -> 1 2 - 1 -> 1 2 1 -
                    while(j_aux<sz-1){
                        tabuleiro[i][j_aux] = tabuleiro[i][j_aux+1];
                        tabuleiro[i][j_aux+1] = tab_aux;
                        j_aux+=1;
                    }

                }

            }
        }
        k++;
    }

}

int jogada(int tabuleiro[][20], int sz, int x, int y){
    int num_quadrados = marcar(tabuleiro, sz, x, y);

    gravidade(tabuleiro, sz);
    coluna(tabuleiro, sz);

    return pontuacao(num_quadrados);
}

void mostrar(int tabuleiro[][20], int sz){
    for(int i=0; i<sz; i++){
        for(int j=0; j<sz; j++){
            if(tabuleiro[i][j]== 0){
                printf("- ");
            }else{
                printf("%d ", tabuleiro[i][j]);
            }

        }
        printf("\n");
    }
}
