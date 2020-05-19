#Distribui os lugares existentes pelos partidos
def ciclo(n_partidos):
	global dados_partidos
	global n_lugares
	idx = 0
	maior_quociente = 0

	while n_lugares > 0:
		while idx < n_partidos:
			dados_partidos[idx][2] = algoritmo(idx)

			if dados_partidos[idx][2] > maior_quociente:
			 	maior_quociente = dados_partidos[idx][2]
			 	quociente_idx = idx
			idx = idx + 1
		
		empate = empate_cotacao(n_partidos, quociente_idx)
		if empate == -1:
			dados_partidos[quociente_idx][1] = dados_partidos[quociente_idx][1] + 1
			maior_quociente = 0
		
		idx = 0
		n_lugares = n_lugares - 1
		
	output()
