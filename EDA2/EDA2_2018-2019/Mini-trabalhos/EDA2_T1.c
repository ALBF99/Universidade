#include <stdio.h>
#include <math.h>

int conta_algarismos(int num)
{
	int conta = 0;

	if (num == 0)
	{
		return 1;
	}

	while(num != 0)
	{
		num = num / 10;
		conta++;
	}

	return conta;
}

int main(void)
{
	int num;
	scanf("%d", &num);

	printf("%d\n", conta_algarismos(num));
	
	return 0;

}