def polyvaleur(listpoly,x):
    n=0
    for i in range(len(listpoly)):
        n+=listpoly[i]*x**i
    return n
print(polyvaleur([1,0,2,3],2))

def Polyaddition(listpoly1,listpoly2):
    L=[]
    for i in range(max(len(listpoly1),len(listpoly2))):
        if i<len(listpoly1) and i<len(listpoly2):
            L.append(listpoly1[i]+listpoly2[i])
        elif i<len(listpoly1):
            L.append(listpoly1[i])
        else:
            L.append(listpoly2[i])
    return L
print(Polyaddition([1,2,5],[3,4]))

def Polyaffiche(listpoly):
    chaine=str(listpoly[0])
    for i in range(1,len(listpoly)):
        if listpoly[i]!=0:
            chaine+="+"+str(listpoly[i])+"X^"+str(i)
    return chaine
print(Polyaffiche([3,0,4,0,2]))
