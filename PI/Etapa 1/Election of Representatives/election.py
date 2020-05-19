#Descobre o partido com mais votos
#Retorna o indice desse partido
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


#Metodo de D'Hondt
#Algoritmo que calcula o quociente do partido
def algoritmo(idx):
	global dados_partidos
	alg = dados_partidos[idx][0] / (dados_partidos[idx][1] + 1 )
	return alg


#Segundo caso de empate
#Caso houver partidos com o mesmo maior quociente
#E houver partidos com o mesmo menor numero de votos
#O lugar e atribuido ao partido com o menor num de votos e de indice
#Retorna o indice desse partido 
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


#Primeiro caso de empate
#Caso houver partidos com o mesmo maior quociente 
#O lugar e atribuido ao partido com menor votos
#Retorna se existe (1) ou nao (-1) qualquer caso de empate
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


#Imprime o output
def output():
	global dados_partidos
	global n_partidos
	
	print("\n")
	for i in range(n_partidos):
		print(dados_partidos[i][1])


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
	n_lugares = 0
	return n_lugares




n_lugares = input()
n_partidos = input()

#indice 0: votos
#indice 1: lugares sentados
#indice 2: quociente
dados_partidos = [[0 for x in range(3)] for y in range(n_partidos)]
n = 0
while n < n_partidos:
	linha = input()

	if linha is None:
		break

	dados_partidos[n][0] = linha
	n = n + 1

ciclo(n_partidos)
