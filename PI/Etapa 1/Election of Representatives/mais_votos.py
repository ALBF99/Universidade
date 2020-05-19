def mais_votos(n_partidos):
	global dados_partidos
	maior_idx = 0
	maior = -1
	n = 0

	while n < n_partidos:
		if maior < dados_partidos[n][0]:
			maior = dados_partidos[n][0]
			maior_idx = n
		n = n + 1

	return maior_idx

