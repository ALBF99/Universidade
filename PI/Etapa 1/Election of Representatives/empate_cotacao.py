def empate_cotacao(n_partidos, quociente_idx):
	global dados_partidos
	global n_lugares

	for i in range(n_partidos):
		
		if i == quociente_idx:
			continue

		else:
			if dados_partidos[i][2] == dados_partidos[quociente_idx][2]:
				menor_votos_idx = menos_votos(n_partidos)
				desempate_idx = empate_votos(n_partidos, menor_votos_idx)
				
				#Caso existir o segundo caso de empate
				if (desempate_idx != -1):
					dados_partidos[desempate_idx][1] = dados_partidos[desempate_idx][1] + 1
					return -1

				else:
					dados_partidos[menor_votos_idx][1] = dados_partidos[menor_votos_idx][1] + 1
					return 1	
			
	return -1
