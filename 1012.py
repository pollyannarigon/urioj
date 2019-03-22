l1 = input().split(" ")
A, B, C= l1


## areatriangulo= base * altura /2
triangulo=(float(A)*float(C)/2)
#area circulo = pi*raio^2
circulo=(3.14159*float(C)**2)
#trapezio base+base * altura /2
trapezio=(((float(A)+float(B))*float(C))/2)
#Quadrado lado^2
quadrado=float(B)**2
#retangulo
retangulo=float(A)*float(B)

print("TRIANGULO: %0.3f" %triangulo)
print("CIRCULO: %0.3f" %circulo)
print("TRAPEZIO: %0.3f" %trapezio)
print("QUADRADO: %0.3f" %quadrado)
print("RETANGULO: %0.3f" %retangulo)
