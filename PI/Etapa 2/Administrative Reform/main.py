#Exercicio 5

def matrizes(file_name):
	# colocar em linhas separadas do input numa lista
	f = open(file_name, "r")
	a = f.readlines()
	matriz = []

	for i in a:
		matriz.append(i.split())
	line1 = matriz.pop(0)
	line2 = matriz.pop(len(matriz)-1)
	f.close()

	#Teste: print (matriz, line1, line2)
	return matriz, line1, line2 

def to_int(matriz, line1, line2):
	#Passar as strings da lista em ints
	for i in matriz:
		i[1] = int(i[1]) 
		i[2] = int(i[2]) 
		i[0] = int(i[0]) 

	line1[0] = int(line1[0])
	line1[1] = int(line1[1])
	line2[0] = int(line2[0])
	line2[1] = int(line2[1])

	#Teste : print(matriz, line1, line2) 
	return matriz, line1, line2

def estradas(matriz, X, Y, C):
	#Descobrir para cada capital o numero de comunidades
	n1 = 0
	n2 = 0
	n3 = 0
	for c in range(C):
		#Teste : print (c)
		l1 = 0
		l2 = 0
		if c == X:
			n1 = n1 + 1
		elif c == Y:
			n2 = n2 + 1	
		else:
			for i in matriz:
				if(i[0] == c and i[1] == X) or (i[0] == X and i[1] == c):
					l1 = i[2]
					#Teste : print(l1)
				elif(i[0] == c and i[1] == Y) or (i[0] == Y and i[1] == c):
					l2 = i[2]
					#Teste : print (l2)
			
			if l1 < l2 and l1 != 0:
				n1 = n1 + 1
			elif l2 < l1 and l2 != 0:
				n2 = n2 + 1
			elif l1 == l2:
				n3 = n3 + 1
			elif l2 == 0 and l1 != 0:
				n1 = n1 + 1
			elif l1 == 0 and l2 != 0:
				n2 = n2 + 1
		#Teste : print(n1, n2, n3)

	return n1, n2, n3

def main1(file_name):
	matriz, line1, line2 = matrizes(file_name)
	matriz, line1, line2 = to_int(matriz, line1, line2)
	C = line1[0]
	X = line2[0]
	Y = line2[1]
	n1, n2, n3 = estradas(matriz, X, Y, C)
	print(n1, n2, n3)
	return n1, n2, n3
