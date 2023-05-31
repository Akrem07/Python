phrase=str(input("donner une phrase: "))
vowels=("aeiouyAEIOUY")
nbrvowels= 0
for i in phrase:
    if(i in vowels):
        nbrvowels=nbrvowels+1
print (nbrvowels)

