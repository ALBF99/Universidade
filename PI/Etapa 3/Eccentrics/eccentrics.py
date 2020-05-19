import sys
import string

def leitura(nome_ficheiro):
	f = open(nome_ficheiro,"r")
	ficheiro = f.read().splitlines()
	f.close()
	return ficheiro

def criar_camadas(ficheiro, max_linhas, n_camadas):
	n_bolas_in = 0
	i = 1
	linha = 0
	camadas_aux = []
	camadas = [[-1]*max_linhas for _ in range(max_linhas)]

	while i<=n_camadas:
		j = 1
		while j<=i:
			k = 1
			while k<=j:
				camadas_aux = ficheiro[linha].split(' ')
				tamanho = len(camadas_aux)

				if tamanho > 1:
					idx = 0
					while idx<tamanho:
						camadas[linha][idx] = int(camadas_aux[idx])
						idx = idx + 1

					n_bolas_in = n_bolas_in + tamanho
					k = k + tamanho

				else:
					n_bolas_in = n_bolas_in + 1
					k = k +1
					camadas[linha][0] = int(camadas_aux[0])

				linha = linha + 1
			j = j + 1
		i = i +1

	return camadas, n_bolas_in
'''
def print_camadas(max_linhas, camadas):
	i = 0
	print("Camadas:")
	while i<max_linhas:
		j = 0
		for j in range(max_linhas):
			print(camadas[i][j]),
			j = j+1

		i = i+1
		print("\n")

'''
def mover_bolas(camadas, max_linhas, n_camadas, l, c, primeiro):
	if l >= max_linhas-n_camadas or l == -1:
		return 

	l_procura = l+1+primeiro
	c_procura = c
	l_aux = -1
	c_aux = -1
	max_peso = -1

	if camadas[l_procura][c_procura] != -1 and camadas[l_procura][c_procura] > max_peso:
		max_peso = camadas[l_procura][c_procura]
		l_aux = l_procura
		c_aux = c_procura

	if camadas[l_procura+1][c_procura] != -1 and camadas[l_procura+1][c_procura] > max_peso:
		max_peso = camadas[l_procura+1][c_procura]
		l_aux = l_procura+1
		c_aux = c_procura

	if camadas[l_procura+1][c_procura+1] != -1 and camadas[l_procura+1][c_procura+1] > max_peso:
		max_peso = camadas[l_procura+1][c_procura+1]
		l_aux = l_procura+1
		c_aux = c_procura+1

	if max_peso == -1:
		return

	camadas[l][c] = max_peso
	camadas[l_aux][c_aux] = -1
	
	#print_camadas(max_linhas, camadas)

	mover_bolas(camadas, max_linhas, n_camadas, l_aux, c_aux, primeiro+1)


def main(nome_ficheiro):
	n = 0
	n_bolas_out = 0

	ficheiro_in = leitura(nome_ficheiro)
	n_camadas = int(ficheiro_in.pop(0))
	max_linhas = int((n_camadas *(n_camadas + 1))/2)
	camadas, n_bolas_in = criar_camadas(ficheiro_in, max_linhas, n_camadas)

	ficheiro = open("output1.txt", "w")
	   
	while n_bolas_out != n_bolas_in:
		ficheiro.write(str(camadas[0][0])+'\n')
		mover_bolas(camadas, max_linhas, n_camadas, 0, 0, 0)
		n_bolas_out = n_bolas_out+1

	ficheiro.close()
	ficheiro_out = leitura("output1.txt")
	return ficheiro_out


if __name__=='__main__':
        main("input1.txt")
