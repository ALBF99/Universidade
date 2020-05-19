#include <stdlib.h> 
#include <stdio.h> 
#include <string.h>
#include "header.h"

struct QNode* new_node(struct pcb *k)
{ 
    struct QNode *temp = (struct QNode*)malloc(sizeof(struct QNode)); 
    temp->processo = k; 
    temp->next = NULL; 

    return temp;
}

void entraNew( int i)
{
	struct QNode *node = new_node(&lista_processos[i]);
	enQueue(queueNew, node);

}


void newToReady()
{
	struct QNode *ptr = deQueue(queueNew);
	enQueue(queueReady, ptr);

}

void readyToRun()
{
	struct QNode *ptr = deQueue(queueReady);
	enQueue(queueRun, ptr);

}

void runToReady()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueReady, ptr);

}

void runToExit()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueExit, ptr);
}

void runToBlock()
{
	struct QNode *ptr = deQueue(queueRun);
	enQueue(queueBlock, ptr);

}

void blockToReady()
{
	struct QNode *ptr = deQueue(queueBlock);
	enQueue(queueReady, ptr);
}

void saidaExit()
{
	deQueue(queueExit);
	
}