casos=int(input())
lista={}
coelhos=0
ratos=0
sapos=0
total=0

for i in range(0, casos, 1):
    entrada=input().split(" ")
    inteiro=int(entrada[0])
    tipo=entrada[1]
    total+=inteiro

    if tipo == "C":
         coelhos=coelhos+inteiro

    if tipo == "R":
         ratos=ratos+inteiro

    if tipo == "S":
         sapos=sapos+inteiro


pcoelhos= (100*coelhos)/total
pratos= (100*ratos)/total
psapos=(100*sapos)/total

print("Total: %d cobaias" %total)
print("Total de coelhos: %d" %coelhos)
print("Total de ratos: %d" %ratos)
print("Total de sapos: %d" %sapos)

print("Percentual de coelhos: %0.2f" %pcoelhos, "%")
print("Percentual de ratos: %0.2f" %pratos, "%")
print("Percentual de sapos: %0.2f" %psapos, "%")
