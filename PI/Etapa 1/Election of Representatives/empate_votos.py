def empate_votos(n_partidos, menor_votos_idx):
	global dados_partidos
	n = 1

	for i in range(n_partidos):
		if i == menor_votos_idx:
			continue

		else:
			if dados_partidos[i][0] == dados_partidos[menor_votos_idx][0] and i < menor_votos_idx:
				return i

	return -1
