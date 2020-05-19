#Exercicio 4


def to_int(arr_F0,arr_F1):
	#Passar as strings das listas da familia em ints
	for i in arr_F0:
		i[1] = int(i[1]) 
		i[2] = int(i[2]) 
		i[0] = int(i[0]) 
	for i in arr_F1:
		i[1] = int(i[1]) 
		i[2] = int(i[2]) 
		i[0] = int(i[0])
	#Teste : print(arr_F0) 
	#Teste : print(arr_F1)
	return arr_F0, arr_F1

def dividir_familias (matriz):
	#dividir a lista matriz por familias 
	arr_F0 = []
	arr_F1 = []
	for i in matriz:
		if i[2] == '0':
			arr_F0.append(i)
		else:
			arr_F1.append(i)
	#Teste : print (arr_F0)
	#Teste : print (arr_F1)
	return arr_F0, arr_F1


def matrizes(file_name):
	# colocar em linhas separadas do input numa lista
	f = open(file_name, "r")
	a = f.readlines()
	matriz = []

	for i in a:
		matriz.append(i.split())
	matriz.pop(0)
	f.close()
	#Teste : print (matriz)
	return matriz

def to_int(arr_F0,arr_F1):
	#Passar as strings das listas da familia em ints
	for i in arr_F0:
		i[1] = int(i[1]) 
		i[2] = int(i[2]) 
		i[0] = int(i[0]) 
	for i in arr_F1:
		i[1] = int(i[1]) 
		i[2] = int(i[2]) 
		i[0] = int(i[0])
	#Teste : print(arr_F0) 
	#Teste : print(arr_F1)
	return arr_F0, arr_F1

def menor(arr_F0, arr_F1):
	#Descobrir a menor distacia entre as duas familias
	m = 1000000000
	for i in arr_F0:
		x1 = i[0]
		y1 = i[1]
		for i in arr_F1:
			x2 = i[0]
			y2 = i[1]
			m1 = abs(x1-x2)+abs(y1-y2)
			if(m1 < m):
				m = m1

	return m

def main1(file_name):
	matriz = matrizes(file_name)
	arr_F0, arr_F1 = dividir_familias(matriz)
	arr_F0, arr_F1 = to_int(arr_F0,arr_F1)
	m = menor(arr_F0, arr_F1)
	print (m)
	return m


