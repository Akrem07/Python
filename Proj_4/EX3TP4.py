dic={}
def text_to_index(txt):
    i=0
    for j in txt.split():
        if j in dic:
            dic[j].append(i)
        else:
            dic[j]=[i]
        i+=1
    return dic
print(text_to_index("ceci est un texte un exemple de texte"))
