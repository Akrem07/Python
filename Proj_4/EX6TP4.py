def ParOuverte(c):
    if c=="(" or c=="{" or c=="[":
        return True
    return False

def ParFermee(c):
    if c==")" or c=="}" or c=="]":
        return True
    return False

def ParAssocie(p):
    if p=="(":
        return ")"
    if p=="{":
        return "}"
    if p=="[":
        return "]"

def cree_pile_vide():
 return [0]

def taille(p):
 return p[0]

def est_vide(p):
 return p==[]

def sommet(p):
 return p[-1]

def depiler(p):
 return p.pop()

def empiler(p,v):
 p.append(v)
 return p

def VerifPar(c):
    pile=[]
    for i in range(len(c)):
        if ParOuverte(c[i]):
            empiler(pile,c[i])
        elif ParFermee(c[i]):
            if est_vide(pile) or sommet(pile)!=ParAssocie(c[i]):
                print("erreur de parenthésage")
            else:
                depiler(pile,c[i])
    if est_vide(pile):
        print("la pile est vide et le parenthésage correct")
    else:
        print("erreur de parenthésage")

print(VerifPar("(a*(b+c))"))
print (VerifPar(")dfdf"))
print(VerifPar("bonjour"))

