entrada=input().split(' ')
n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])


lista=[n1, n2, n3]

ordenados=sorted(lista, key=float, reverse=True)
#lista.sort(key=float, reverse=True)
'''
print(ordenados)
print(ordenados[0])
print(ordenados[1])
print(ordenados[2])
'''
a=ordenados[0]
b=ordenados[1]
c=ordenados[2]
a2=a*a
b2=b*b
c2=c*c


if a >= (b+c):
    print("NAO FORMA TRIANGULO")

else:
    if a2 == b2+c2:
        print("TRIANGULO RETANGULO")
    if a2 > b2+c2:
        print("TRIANGULO OBTUSANGULO")
    if a2 < b2+c2:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b != c:
        print("TRIANGULO ISOSCELES")
    elif a == c != b:
        print("TRIANGULO ISOSCELES")
    elif b == c != a:
        print("TRIANGULO ISOSCELES")
