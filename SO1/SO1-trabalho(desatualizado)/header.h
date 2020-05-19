#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#define MEM_SIZE 300

struct pcb
 {
 	int pid;
 	int *pc;
 	int estado;

 	//Dados extras:
 	int *localizador_instrucoes;
 	int tempo;
 	
	int tempoBlock;
	int tempoRun;
	int tempoNew;
	int tempoExit;

 };

struct QNode 
{ 
    struct pcb *processo; 
    struct QNode *next; 

}; 

struct Queue 
{ 
    struct QNode *front, *rear;

}; 
//Queue_LL.c
struct QNode* new_node(struct pcb *k);
struct Queue *createQueue();
void enQueue(struct Queue *q, struct QNode *k);
struct QNode *deQueue(struct Queue *q);

//Mudanca_estado.c
void entraNew(int i);
void newToReady();
void readyToRun();
void runToReady();
void runToExit();
void runToBlock();
void blockToReady();
int saidaExit();

//Fase2.c
int MEM[MEM_SIZE];
struct pcb *lista_processos;
char *aux_ficheiro[20];
int n_processos;
//Queue para cada estado 
struct Queue *queueNew; 
struct Queue *queueReady;
struct Queue *queueRun; 
struct Queue *queueBlock; 
struct Queue *queueExit;  



int atoi(const char *str);