a= input()
a=int(a)
l=[]
for b in range (a):
    l.append((input()))
v=['a','e','i','o','u']
vowel=[]
consonent=[]
for b in range (0,len(l)):
    if l[b].isalpha():
        if l[b] in v:
            vowel.append(l[b])
        
        else:
            consonent.append(l[b])
        
print (vowel)
print (consonent)
