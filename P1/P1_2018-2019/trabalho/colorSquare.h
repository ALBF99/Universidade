

#ifndef COLOR_SQUARES_COLORSQUARE_H
#define COLOR_SQUARES_COLORSQUARE_H

#endif //COLOR_SQUARES_COLORSQUARE_H
#include <stdio.h>
#include <string.h>

int rand(void);
int atoi (char *const);
int contaZeros(int tabuleiro[][20], int sz);
int marcar (int tabuleiro[][20], int sz, int x, int y);
int pontuacao(int num_quadrados);
void gravidade(int tabuleiro[][20], int sz);
void coluna(int tabuleiro[][20], int sz);
int jogada(int tabuleiro[][20], int sz, int x, int y);
void mostrar(int tabuleiro[][20], int sz);
void iterativo();
void automatico();