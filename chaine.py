
ch=str(input("Donner une chaine de caractère: "))
L=list(ch)

for  i in range(len(L)):           
    if ord('a')<= ord(L[i])<=ord('z'):       
        L[i]=chr(ord(L[i])-(ord('s')-ord('S')))
print("la sortie est:", "".join(L))
