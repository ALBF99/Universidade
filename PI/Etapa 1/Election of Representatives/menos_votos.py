#descobre o partido com menos votos
#Retorna o indice desse partido
def menos_votos(n_partidos):
	global dados_partidos
	menor_idx = 0
	menor = 1000000
	n = 0
	
	while n < n_partidos:

		if dados_partidos[n][0] < menor:
			menor = dados_partidos[n][0]
			menor_idx = n

		n = n +1

	return menor_idx
