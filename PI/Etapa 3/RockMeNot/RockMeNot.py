def possivel(a,x,y,c,l):
        count = 0
        if x != 0:
                if y != 0:
                        if a[x-1][y-1]=='#':
                                count+=1
                if y != c:
                        if a[x-1][y+1]=='#':
                                count+=1
                if y == 0 or y == c:
                        count+=1
        if x != l:
                if y != 0:
                        if a[x+1][y-1]=='#':
                                count+=1
                if y != c:
                        
                        if a[x+1][y+1]=='#':
                                count+=1
                if y == 0 or y == c:
                        count+=1
        if x == 0 or x == l:
                
                        count+=1                        
        if count <= 2:
                return True
        return False



def count(a,c,l):
        c1=c-1
        l1=l-1
        valor=0
        for i in range(l):
                for j in range(c):
                        if a[i][j] != '#':
                                num = possivel(a,i,j,c1,l1)
                                if num == True:
                                        a[i][j] = '#'
                                        valor+=1
        return valor


def matriz(a):
        
        txt = a[0]
        txt = txt.replace("\n","")
        txt = txt.split()
        c = int(txt[0])
        l = int(txt[1])

        d = [[0 for x in range(c)] for y in range(l)]

        for i in range(l+1):
                if i>=1:
                        intime = a[i]
                        intime = intime.replace("\n","")
                        for j in range(c):
                                i-=1
                                d[i][j] = intime[j:j+1]
                                i+=1
        return d,c,l

def solve(a):
        d,c,l= matriz(a)
        return count(d,c,l)
