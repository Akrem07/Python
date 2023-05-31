Nb_jours=[31,28,31,30,31,30,31,31,30,31,30,31]
Mois=['janvier','Février','Mars','Avril','Mai','Juin','juillet','Aout','Septembre','Octobre','Novembre','Décember']
T1 = Nb_jours[:]
T2 = Mois[:]
print(T1)
print(T2)
T3 = []
for i in range(len(Mois)):
    T3.append(T2[i])
    T3.append(T1[i])
print(T3)