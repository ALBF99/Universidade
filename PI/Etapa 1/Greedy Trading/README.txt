Objectivo:
	Desenvolva uma ferramenta que receba atualizações sobre a variação de preço de um determinado instrumento CDF e que seja capaz de responder a consultas sobre as seqüências com soma máxima e seu valor mediano.

Input:
	Uma sequência de N-linhas iniciando por u, q ou x. Linhas começando com u denotam atualizações, onde o caractere u é seguido por um único espaço e um número inteiro k. Uma linha iniciada com q indica um comando de consulta e uma linha iniciada com x deve encerrar a ferramenta. Todas as entradas começam com um comando de atualização.

Output:
	Somente o comando q produz saída. A saída é uma única linha com três números inteiros:
		• Dois números inteiros que indicam a posição inicial e a posição final da subsequência contígua não vazia com a soma máxima em relação à sequência de números recebidos até agora. Suponha que as atualizações sejam numeradas da posição 0 (consulte a saída de amostra abaixo). Observe que, se houver duas ou mais dessas subsequências, você deve enviar informações sobre a última subsequência. Por última subsequência, queremos dizer aquele que termina em uma posição posterior e, se mais de uma subsequência termina na mesma posição, queremos o que começa em uma posição posterior. 
		• O terceiro número inteiro indica a mediana dessa subsequência. Observe que, caso esse comprimento de sequência seja igual, você deverá gerar o maior dos dois valores do meio.

