#include <stdio.h>
#include "colorSquare.h"

int main(){
    char modo;
    printf("Bem vindo, ao jogo COLOR SQUARE!\n");
    printf("A -> Modo Automático\n");
    printf("I -> Modo Iterativo\n");
    printf("Selecione um modo:");
    scanf("%c", &modo);

    if(modo=='A'){
        automatico();
    }
    else if(modo=='I'){
        iterativo();
    }

    return 0;
}
