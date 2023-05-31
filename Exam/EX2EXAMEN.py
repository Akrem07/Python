class Date:
    nb_jour=(31,28,31,30,31,30,31,31,30,31,30,31)
    def __init__(self,Jour,Mois,Année) -> None:
        self.Jour=Jour
        self.Mois=Mois
        self.Année=Année
        if self.Mois>12 and self.Mois<1:
            print("Mois invalide")
        elif self.Jour>Date.nb_jour[Mois] and self.Jour<1:
            print("Jour invalide")
        elif len(str(self.Année))!= 4:
            print("Année invalide")
        self.nb_jour=Date.nb_jour

    def Affiche_date(self):
        return print("{}/{}/{}".format(self.Jour,self.Mois,self.Année))

class Adresse:
    def __init__(self,Num,Code_postal,Ville,Rue) -> None:
        self.Num=Num
        self.Rue=Rue
        self.Code_postal=Code_postal
        self.Ville=Ville
        if len(str(self.Rue)) != 2:
            print("Rue invalide")

    def Affiche_adresse(self):
        return print("{} {} {} {}".format(self.Num,self.Code_Rue,self.Ville))


class Personne:
    def __init__(self,Nom,Date_naissance,Adresse,) -> None:
        self.Nom=Nom
        self.Date_naissance=Date_naissance
        self.Adresse=Adresse
        self.__Age__=(2022-self.Date_naissance)

    def Affiche_personne(self):
        return print("{} habite à {} né le {} agé de {} ans".format(self.Nom,self.Adresse,self.date_naissance,self.Age))


class Etudiant(Personne):
    def __init__(self,Nom,Date_naissance,Adresse,Filiére):
        super().__init__(Nom,Date_naissance,Adresse)
        self.Filiére=Filiére

    def __str__(self):
        return print("{} est un étudiant, et sa filière est {}".format(self.Nom,self.Filiére))
s=Etudiant("akrem",12/7/2000,"espagne","EEA")
print(s)