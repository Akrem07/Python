class Date():
    def __init__(self,jour,mois,annee) -> None:
        self.jour=jour
        self.mois=mois
        self.annee=annee
    def __str__(self) -> str:
        return print("la date est ".format(self.jour,self.mois,self.annee))

class Livre:
    num_livre=0

    def __init__(self,t,nb_ex):
        self.num=Livre.num_livre
        self.titre=t
        self.nb_exemplaires=nb_ex
        Livre.num_livre+=1

    def __str__(self):
        return print("« Livre N° {}; intitulé : {}; {} exemplaires disponibles »".format(self.num,self.titre,self.nb_exemplaires))

    def est_disponible(self):
        if self.nb_exemplaire>0:
            return True
        return False

    def retirer_un_exemplaire(self):
        if self.nb_exemplaires>0:
            self.nb_exemplaires-=1
        else:
            print("le stocke est déja epuisé")

    def retour_exemplaire(self):
        self.nb_exemplaires+=1

class Abonné:
    NCIN=[]
    def __init__(self,Ncin,Nom,Est_pénalisé,Nb_emprunt):
        if (Ncin not in Abonné.NCIN):
            self.Ncin=Ncin
            self.Nom=Nom
            self.Est_pénalisé=Est_pénalisé
            self.Nb_emprunt=Nb_emprunt
            print("Abonné est ajouter avec succés")
        else:
            print("l'Abonné existe déjà")

    def __str__(self):
        return print("« NCIN: {} ; Nom: {} ; etat: {} »".format(self.Ncin,self.Nom,self.Est_pénalisé))

    def est_pénalisé(self):
        if self.Est_pénalisé:
            return True
        return False

    def donner_Ncin(self):
        return self.Ncin

    def pénaliser(self):
        return self.est_pénalisé


    def marquer_retour(self):
        if self.Nb_emprunt>0:
            self.Nb_emprunt-=1

    def marquer_emprunt(self):
        self.Nb_emprunt+=1


class Abonné_restreint(Abonné):
    def __init__(self, Ncin, Nom, Est_pénalisé, Nb_emprunt,borne_max_emprunt):
        super().__init__(Ncin, Nom, Est_pénalisé, Nb_emprunt)
        self.borne_max_emprunt=borne_max_emprunt

    def __str__(self):
        pénaliser="n'est pas penalisé"
        if(self.est_pénalisé):
            pénaliser="est penalisé"
        return print("NCIN: {0}\n Nom: {1}\n Etat: {2}\n Nbr_Emprunt: {3}\n".format(self.Ncin,self.Nom,pénaliser,self.borne_max_emprunt))

    def marquer_emprunt(self):
        if (self.Nb_emprunt<self.borne_max_emprunt):
            self.Nb_emprunt+=1
        else :
            print("désolé, vous avez atteint le nombre maximum de emprunts")


class Emprunt:
    def __init__(self,Num_livre,Ncin_abonné,De) :
        self.Num_livre=Num_livre
        self.Ncin_abonné=Ncin_abonné
        self.De=De
        self.Dpr=De+10
        self.Pénalitré=False

    def maj_pénalit(self,da):
        if self.Dpr > self.Da+10:
            self.pénalité=True


class bibliothèque:
    def __init__(self):
        self.Livres={}
        self.Emprunteurs={}
        self.Opérations={}
    
    def ajouter_livre(self,l):
        if l.num in self.livres:
            print("ce livre est déjà inseré")
        else:
            self.livres[l.num]=l

    def ajouter_abonné (self,a):
        if a.Ncin in self.Emprunteurs:
            print("cet abonné existe déjà")
        else:
            self.Emprunteurs[a.Ncin]=a

    def __str__(self) -> str:
        return ("Livres {}\nEmprunteurs {}\nOpérations {}\n".format(self.Livres,self.Emprunteurs,self.Opérations))

    def livres_empruntés (self, ncin):
        livres=[]
        for i in self.Opérations.keys():
            if i[0]==ncin:
                livres.append(i[1])
        return livres

    def ont_emprunté (self, num_liv):
        abonnes=[]
        for i in self.Opérations.keys():
            if i[1]==num_liv:
                abonnes.append(i[1])
        return abonnes
    def emprunter (self, ncin, num_liv, date_emprunt):
        if (ncin not in self.Emprunteurs):
            print("ce personne n'est pas abonné")
        else:
            Abonné=self.Emprunteurs[ncin]
        
    


