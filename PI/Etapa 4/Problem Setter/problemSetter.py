def leitura(nome_ficheiro): #leitura do input
    f = open(nome_ficheiro,"r")
    escolhas = f.read().splitlines()
    return escolhas 

def divisao(equipas): #dividir o input em equipas separadas
	ret = []
	aux = []
	for i in equipas:
		aux = i.split(' ')
		for j in range(len(aux)):
			aux[j] = int(aux[j])
		ret.append(aux)
	return ret

def ordenar(equipas): #ordenar as equipas pelo inicio dos intervalos de separacao, usando insertionsort
	for i in range(1, len(equipas)):
		chave = equipas[i][1]
		chave_inteira = equipas[i]
		j = i-1
		while j>= 0 and chave< equipas[j][1]:
			equipas[j+1] = equipas[j]
			j-=1
		equipas[j+1] = chave_inteira

	return equipas 

def verificar_abertos(dia, equipas,abertos): #as equipas que é possivel mandar emails
	for i in equipas:
		if dia == i[1]:
			abertos.append(i)
	return abertos


def deadline_maisProximo(equipas): #ver qual o deadline mais proximo
	atual = 31
	equipa = []
	if len(equipas) == 1:
		return equipas[0]
	for i in equipas:
		if i[2] < atual: 	
			atual = i[2]
			equipa = i
	return equipa

def verificar_data(dia,equipas): #ver se a equipa com o deadline+prox já está "preparada" para receber emails
	if len(equipas)==0:
		return 0
	equipa = deadline_maisProximo(equipas)
	iniciar = (equipa[2]+1)- equipa[0]
	if iniciar == dia:
		return 1
	else:
		return 0
	
def decrementar(equipas): #decrementa o numero de emails por mandar, e remove da lista
	for i in equipas:
		i[0]-=1
	return equipas

def remover_equipas(abertos, equipas): #remover as equipas que estão no abertos
	for i in abertos:
		if i in equipas:
			equipas.remove(i)
	return equipas


def main(nome_ficheiro):
	abertos=[]
	mails_send = 0
	num_dias = 0
	dia = 1

	equipas = leitura(nome_ficheiro)
	num_equipas = int(equipas.pop(0))
	equipas = ordenar(divisao(equipas))

	while(num_equipas>0):
		out = []
		abertos = verificar_abertos(dia,equipas,abertos)
		equipas = remover_equipas(abertos,equipas)
		mails_send = verificar_data(dia, abertos)

		if mails_send==1:
			abertos = decrementar(abertos)
			num_dias+=1	

		for k in abertos:
			if k[0]==0:
				num_equipas-=1
				out.append(k)

		abertos = remover_equipas(out,abertos)
		dia+=1

	return num_dias

