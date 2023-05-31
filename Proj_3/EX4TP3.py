D=[]
n=int(input("donner la taille de la liste: "))
while n<6 or n>50:
    n=int(input("donner la taille de la liste: "))
for i in range(n):
    b=int(input("donner l'entier numero {} ".format(i+1)))
    D.append(b)
print(D)
R=[]
s=0
for i in D:
    s+=i
    R.append(s)
print(R)
#2
l=[]
x=float(input("donner un réel: "))
a=str(x)
x=a.index(".")
a=a[x+1:]
for i in range(len(a)):
    l.append(int(a[i]))
print(l)




