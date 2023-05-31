dic={}
def Saisie(n):
    for i in range(n):
        nom=str(input("donner le nom de la produit {}: ".format(i+1)))
        Prix=float(input("donner le prix de la produit{}: ".format(i+1)))
        dic[nom]=(Prix)
    return dic
print(Saisie(3))

def Disponibilité(Prod,Prix):
    if Prod in dic:
        return True
    return False
print(Disponibilité("aa",10))

def Prix_moy():
    somme=0
    for i in dic:
        somme+=dic[i]
    return somme/len(dic)
print(Prix_moy())

def Fourchette_prix(Mini,Maxi):
    for i in dic:
        if dic[i]>=Mini and dic[i]<=Maxi:
            print(i)
Fourchette_prix(11,20)

Pan={}
def Sais_Pan(n):
    for i in range(n):
        nom=str(input("donner le nom de la produit {}: ".format(i+1)))
        Qnatité=int(input("donner la quantité de la produit {}: ".format(i+1)))
        Pan[nom]=(Qnatité)
    return Pan
print(Sais_Pan(2))

def Tous_disponible():
    for i in Pan:
        if i in dic:
            return True
        return False
print(Tous_disponible())

def Prix_achats():
    somme=0
    for i in Pan:
        somme+=dic[i]*Pan[i]
    return somme
print(Prix_achats())





