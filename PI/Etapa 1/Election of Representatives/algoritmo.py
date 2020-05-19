#Metodo de D'Hondt
#Algoritmo que calcula o quociente do partido
def algoritmo(idx):
	global dados_partidos
	alg = dados_partidos[idx][0] / (dados_partidos[idx][1] + 1 )
	return alg
