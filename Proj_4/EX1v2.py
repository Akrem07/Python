from random import randint
l=[]
def listAleaInt(n,a,b):
    for i in range (n):
        l.append(randint(a,b))
    return l
l=listAleaInt(6,5,30)
print(l)

x=l.index(min(l))
print("l'indice de la case qui contient le minimum de la liste {} est {}".format(l,x))

print("la liste avant le changement est ",l)
l[0],l[x]=l[x],l[0]
print("la liste avant le changement est ",l)
