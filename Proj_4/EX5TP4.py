def Valide(DNA):
    adn=["A","T","G","C","a","t","g","c"]
    for i in range (len(DNA)):
        if ( DNA[i] in adn ):
            i+=1
        else:
            return False
    return True
print(Valide("agT",))

def Saisie():
    ch=str(input("donner une chaine d'ADN: "))
    while Valide(ch)== True :
        return ch
    print("erreur de saisie de l'ADN")
print(Saisie())

def Proportion(ch1,ch2):
    return ch2.count(ch1)
ch=Saisie()
sq=Saisie()
n=0
for i in range(len(ch)-1):
    if (sq == ch[i]+ch[i+1]):
        n+=1
    i+=1
print("Il y a {} '{}' dans votre chaine ".format(n,sq))
