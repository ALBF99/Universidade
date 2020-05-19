

#pontos2=[[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6],[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]]
#pontos=[[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]]

#size = 7
#size = 4
#pontos=[[0,0],[1,0],[1,1],[0,1]]
#pontos2=[[0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1]]

def matrizes(file_name):
    # colocar em linhas separadas do input numa lista
    f = open(file_name, "r")
    a = f.readlines()
    matriz = []
    for i in a:
        matriz.append(i.split())
    size1 = matriz.pop(0)
    size = int(size1[0])
    for i in matriz:
        i[1] = int(i[1]) 
        i[0] = int(i[0]) 
    f.close()
    return matriz,size

def recebecalcula(pontos,size):
    import numpy as np
    x = np.array(pontos[0])
    y = np.array(pontos[1])
    for i in range(int((size-1)/2)):
        x = np.append(x, pontos[(i*2)+2])
        y = np.append(y, pontos[(i*2)+3])
    return PolyArea(x,y)

def PolyArea(x,y):
    import numpy as np
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def resolve_matriz(P1,P2,P3,P4):
    import numpy as np
    
    x1,y1=P1
    x2,y2=P2
    x3,y3=P3
    x4,y4=P4

    X=x2-x1
    Y=y2-y1
    XX=-1*(x4-x3)
    YY=-1*(y4-y3)
    xr=x3-x1
    yr=y3-y1
    
    A = np.array([[X,XX],[Y,YY]])
    B = np.array([[xr],[yr]])
    
    if np.linalg.det(A)!=0:
        #print(np.linalg.solve(A,B))
        return np.linalg.solve(A,B)
    if np.linalg.det(A)==0:
        #print([[-1][-1]])
        return [[-1][-1]]

def verifica(x):
    if x[0]<0 or x[0]>1 or x[1]<0 or x[1]>1:
        return False
    return True


def calcula_areaponto(pontos,pontos2,size):
    import numpy as np
    from shapely.geometry import Point, Polygon
    
    countp = 0
    poly = Polygon(pontos)
    area = 0
    areaponto = []
    for i in range(size):
        armazena = np.array(pontos2[i])
        pcertos = 0
    
        for x in range(size-1):
            inside = 0
            countp=0

            for y in range(size):
                if verifica(resolve_matriz(pontos2[i],pontos2[i+x+1],pontos2[y],pontos2[y+1])) == True:
                    countp+=1
            if countp <= 4:
                p1x = (pontos2[i][0] + pontos2[i+x+1][0])/2
                p1y = (pontos2[i][1] + pontos2[i+x+1][1])/2
                p1 = Point(p1x,p1y)
            
                if p1.within(poly) or p1.intersects(poly):
                    armazena = np.append(armazena, pontos2[i+x+1])
                
        if recebecalcula(armazena,(len(armazena)-1)) == area:
            areaponto.append(i)
        if recebecalcula(armazena,(len(armazena)-1)) > area:
            area = recebecalcula(armazena,(len(armazena)-1))
            areaponto = [i]
    return areaponto

def calcula_save_distance(pontos2, areaponto):
    import numpy as np
    
    distancebase = np.linalg.norm(np.array((0,0))-np.array(pontos2[areaponto[0]]))
    savedistance = []
    for d in range(len(areaponto)):
        distance = np.linalg.norm(np.array((0,0))-np.array(pontos2[areaponto[d]]))
        if distance==distancebase:
            savedistance.append(d)
        if distance<distancebase:
            savedistance=[d]
    return savedistance

def calcula_pontofinal(pontos2, areaponto):
    savedistance = calcula_save_distance(pontos2, areaponto)
    checkx = 0
    countdistance = 0
    if len(savedistance)>1:
        for r in savedistance:
            sx, sy = pontos2[areaponto[savedistance[countdistance]]]
            if checkx>sx:
                checkx=countdistance
            countdistance+=1
    return pontos2[areaponto[savedistance[checkx]]]

def arrayduplo(pontos):
    pontos2 = []
    for i in range(2):
        for i in range(len(pontos)):
            pontos2.append(pontos[i])
    return pontos2

def solve(file_name):
    pontos, size = matrizes(file_name)
    pontos2 = arrayduplo(pontos)
    areaponto = calcula_areaponto(pontos,pontos2,size) 
    return calcula_pontofinal(pontos2, areaponto)

