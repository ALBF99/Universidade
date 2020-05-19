#include <stdio.h>
#include <string.h>
#include "colorSquare.h"

void automatico(){

    FILE *pToFile;

    char nomef[50];
    printf("\nNome do ficheiro:");
    scanf(" %s" , nomef);
    pToFile = fopen(nomef, "r");


    //Verifica se existe esse ficheiro
    while(pToFile==NULL){
        printf("Erro, não foi possível abrir o ficheiro\n");
        printf("Nome do ficheiro:");
        scanf(" %s" , nomef);
        pToFile = fopen(nomef, "r");
    }

    //Processa o tamanho do tabuleiro
    char sz[5];
    fscanf(pToFile,"%s\n", sz);
    int size = atoi(sz);

    //Processa o tabuleiro
    char tab_str[size];
    int tab[20][20];
    for(int i=0; i<size; i++){
        fscanf(pToFile, "%s \n", &tab_str[i]);

        int j=i;
        int k=0;
        while(j<size+i){
            tab[i][k]=tab_str[j]-'0';
            j++;
            k++;
        }
    }

    //Processa o numero de movimentos
    char num_mov[5];
    fscanf(pToFile,"%s\n", num_mov);
    int movimentos =atoi(num_mov);

    //Processa os movimentos
    char mov[500];
    fgets(mov, 500, pToFile);

    int a=0;
    int b=2;
    int x, y;
    int aux;
    int total=0;
    while(movimentos>0){
        x=mov[a]-'0';
        y=mov[b]-'0';
        a=a+5;
        b=b+5;

        int y_aux=(size-1)-y;
        int x_real = y_aux;
        int y_real = x;

        movimentos--;

        if(tab[x_real][y_real]!=0 && x_real<size && y_real<size){
            aux = jogada(tab, size, x_real, y_real);
            total = total + aux;


        }
        if(movimentos==0){
            printf("Pontuação:%d \n\n",total);
        }

    }
    fclose(pToFile);

}

