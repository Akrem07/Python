L=[]
T=int(input("donner la taille de la liste: "))
for i in range(T):
    E=int(input("donner un entier: "))
    L.append(E)
print(L)
print("la somme des elements de la liste l est ",sum(L))
print("la valeur maximale de la liste l est ",max(L))
print("la valeur minimale de la liste l est ",min(L))

