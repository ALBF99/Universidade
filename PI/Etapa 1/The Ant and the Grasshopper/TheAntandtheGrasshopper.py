"""
MIUP 2016 Problem B:
The Ant and the Grasshopper

Debito -> D
Anos -> A
Juros (Percentagem) -> j
Juros (1+j) -> J
Pagamento Total -> T

Exemplo:
Q a quantia fixa a pagar a cada ano

T(0)= D
T(1)=T(0)*(1+j)-Q

Caso Geral:

T(A)=T(A-1)*(1+j)-Q

Logo é possível verificar que é uma soma de progressão geometrica;

Se considerar-mos que depois emprestimo fica tudo a zeros, é possível dizer:

0=D*(J**A)-Q*((1-(J**A))/(1-J))

Q=(D*(J**A)*(1-J))/(1-(J**A))

Logo o total a pagar será o número de anos vezes a quantidade fixa, e com isto temos a "fórmula final":

T =(A*D*(J**A)*(1-J))/(1-(J**A))


"""
def testes(x):
    import filecmp
    
    with open(x,'r')as f:
        a = f.readlines()
        f.close()
        
    arrayduplo = []
    number = 0

    number = int(a[0])
    number2 = number
    number3 = 0
    i=0

    while(number>0):
        number-=1
        counter = 0
        while counter != 3:
            i+=1
            counter = 0
            put = a[i]
            put = put.split(' ')
            A = put[0]
            D = put[1]
            j = put[2]
            A = float(A)
            D = float(D)
            j = float(j)
            if A >= 1 and A <= 100:
                counter = counter + 1
            if D > 0 and D <= 1000:
                counter = counter + 1
            if j > 0 and j <= 100:
                counter = counter + 1
        number3 = number3 + 1
        arrayduplo.append(put)
    
    final = ''
    while (number != number2):
            A = arrayduplo[number][0]
            D = arrayduplo[number][1]
            j = arrayduplo[number][2]
            A = float(A)
            D = float(D)
            j = float ((float(j))*0.01)
            J = 1 + j
            T = (A*D*(J**A)*(1-J))/(1-(J**A))
            T = round(T*1000)
            T = float(T/1000)
            final = final + str(T) + '\n'
            number+=1
            
    file = open("resultado.txt", "w")
    file.write(final)
    file.close()
    
    if x=='teste1.txt':
        return filecmp.cmp('res1.txt','resultado.txt')
    elif x=='teste2.txt':
        return filecmp.cmp('res2.txt','resultado.txt')


