import random

######################################################################################################
# codigo_aleatorio - Esta função gera um código aleatório de 4 algarismos, sem repetição.
#
# Argumentos:
# Não tem argumentos
#
# Valor de retorno:
# código com 4 algarismos, str
######################################################################################################

def codigo_aleatorio():
	a=str(int(random.random()*10))
	b=str(int(random.random()*10))
	c=str(int(random.random()*10))
	d=str(int(random.random()*10))
	while a==b or a==c or a==d:
		a=str(int(random.random()*10))
	while b==c or b==d or b==a:
		b=str(int(random.random()*10))
	while c==d or c==a or c==b:
		c=str(int(random.random()*10))
	while d==a or d==b or d==c:
		d=str(int(random.random()*10))
	code=a+b+c+d
	return code
	
#######################################################################################################
# jogo - Esta função indica o número de acertos, ou seja, indica o número de algarismos nas posições 
# certas (touros) e o número de algarismos certos em posições diferentes (porcos).
#
# Argumentos:
# aleatorio - código com 4 algarismos gerado pela função codigo_aleatorio, str
# code - input do utilizador, str
#
# Valor de retorno:
# número de touros e porcos, str
#######################################################################################################

def jogo(aleatorio,code):
	bulls=0
	for i in range (len(code)):
		if code[i]==aleatorio[i]:
			bulls=bulls+1
	pigs=0
	for i in range(len(code)):
		for x in range(len(aleatorio)):
			if code[i]==aleatorio[x]:
				pigs=pigs+1
	pigs=pigs-bulls
	
	if bulls==0:
		return(str(pigs)+'P'+'')
	elif pigs==0:
		return (str(bulls)+'T'+'')
	else:
		return(str(bulls)+'T'+' '+str(pigs)+'P'+' ')

#######################################################################################################
# regras_do_jogo - Esta função descreve as regras do jogo
#
# Argumentos:
# Não tem argumentos
#
# Valor de retorno:
# regras do jogo, str
######################################################################################################

def regras_do_jogo():
	a=' '*5+'PIGS AND BULLS\n'
	b='O computador gera um código de 4 algarismos entre 0 e 9, sem repetição.\n'
	c='O objetivo deste jogo é adivinhar esse código, para isso o jogador vai fazendo várias tentativas até acertar.\n'
	d='Em cada tentativa o programa devolve o nº de acertos.\n'
	e='Se os algarismos estão nas posições certas, o programa indica o nº de touros(T).\n'
	f='E se os algarismos certos estão em posições diferentes, o programa indica o nº de porcos(P).\n'
	g='Por exemplo:\n'
	h='Se o código for 4271 e a tentativa for 1234, a resposta deve ser 1T, 2P (o touro é ”2”, os porcos são ”4” e ”1”).\n'
	i='Vamos jogar?'
	return a+b+c+d+e+f+g+h+i

######################################################################################################
# validade_code - Esta função avalia a validade do input do utilizador
#
# Argumentos:
# my_guess - input do utilizador, str
# 
# Valor de retorno:
# Invalidez do código, str
######################################################################################################

def validade_code(my_guess):
	alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for i in range(len(alfabeto)):
		for x in range(len(my_guess)):
			if my_guess[x]==alfabeto[i]:
				return'Código inválido'
				
	if len(my_guess)!=4:
		return 'Código inválido'
	elif my_guess[0]==my_guess[1] or my_guess[0]==my_guess[2] or my_guess[0]==my_guess[3] or my_guess[1]==my_guess[2] or my_guess[1]==my_guess[3] or my_guess[2]==my_guess[3]:
		return 'Código inválido'
	


print(regras_do_jogo())
code=codigo_aleatorio()
my_guess=0
tentativas=0
a=''
b=''
while my_guess!=code:
	my_guess=input('\nCódigo?')
	if validade_code(my_guess):
		print (validade_code(my_guess))
		continue
		
	tentativas=tentativas+1
	a=''+'T'+str(tentativas)+':'+ my_guess + ','+ jogo(code, my_guess)+ '\n'
	b=b+a
	
	if my_guess == code:
		print('Acertou!!!') 
		print('\nAs tuas tentativas foram: \n'+b)
	else:
		print(jogo(code,my_guess))






