#4220 480

maior=0
lista={}
pos=1
while pos < 101:
    entrada=int(input())
    if entrada>maior:
        maior=entrada
        lista[entrada]=pos
    pos+=1


print(maior)
print(lista[maior])
