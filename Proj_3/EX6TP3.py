A=[]
B=[]
S=[]
c=int(input("donner le nombre des colonnes: "))
l=int(input("donner le nombre des lignes: "))
for i in range (0,l):
    z=[]
    for j in range (0,c):
        x=int(input("donner l'entier numero {}: ".format(i+1)))
        z.append(x)
    A.append(z)
for i in range (0,l):
    z=[]
    for j in range (0,c):
        x=int(input("donner l'entier numero {}: ".format(i+1)))
        z.append(x)
    B.append(z)
print(A)
print(B)
for i in range (0,l):
    Sum=[]
    for j in range (0,c):
        y=A[i][j]+B[i][j]
        Sum.append(y)
    S.append(Sum)
print(S)

