phrase=str(input("donner une phrase: "))

percentage = {}

for i in phrase :
    if i in percentage:
        percentage[i] += 1
    else :
        percentage[i] = 1
for word,number in percentage.items():
    print("le pocentage du caractére {} est: {}%".format(word,(number/len(phrase)*100),10))

