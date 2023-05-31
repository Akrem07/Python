liste=[]
T=int(input("donner la taille de la liste: "))
for i in range(T):
    E=int(input("donner l'entier num {}: ".format(i+1)))
    liste.append(E)
def differences(l):
    M=[]
    for i in range(len(l)-1):
        M.append(l[i+1]-l[i])
    return M
print(differences(liste))
print("**********************")
def itere(l,n):
    x=[]
    if n==0 :
        return l
    elif n==1:
        return differences(l)
    else :
        for k in range (n-1):
            x=differences(l)
            l=x
        return differences(x)
n=int(input("donner un entier naturel positif: "))
liste_1=itere(liste,n)
print(liste_1)