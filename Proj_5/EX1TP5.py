class Rectangle:
    def __init__(self,longueur,largeur):
        self.nom      = "rectangle"
        self.longueur = longueur
        self.largeur  = largeur

    def surface_tri(self):
        return ((self.longueur*self.largeur)/2)

    def __str__(self):
        return ("la surfece du triangle qui a un longueur {0} et un largeur {1} est {2} ".format(self.longueur,self.largeur,(self.surface_tri())))


class Carre (Rectangle):
    def __init__(self, longueur, largeur):
        super().__init__(longueur, largeur)
        self.nom='carre'
    def surface_car(self):
        return (self.longueur*self.largeur)

    def __str__(self):
        return ("la surfece du carre qui a un longueur {} et un largeur {} est {} ".format(self.longuer,self.largeur,self.surface_car()))

class Point ():
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def __str__(self) -> str:
        return ("les coordonnées de la point est ({};{})".format(self.x,self.y))

class Segment ():
    def __init__(self,x2,y2,x1=0,y1=0):
        self.orig=Point(x1,y1)
        self.exterem=print(x2,y2)
    def __str__(self) -> str:
        return ("la point qui est a l'extrimiter a les coordonnees {0} la point qui est situer a l'origine a les coordonnees {1}".format(self.orig,self.exterem))
s=Segment(1,2,3,4)
print(s)

r=Rectangle(4,5)
print(r)