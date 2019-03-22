'''
cod1=int(input())
num1=int(input())
valor1=float(input())

cod2=int(input())
num2=int(input())
valor2=float(input())


apagar=float((num1*valor1)+ (num2*valor2))
'''


l1 = input().split(" ")
l2 = input().split(" ")

cod1, num1, valor1 = l1
cod2, num2, valor2 = l2

apagar = (int(num1) * float(valor1)) + (int(num2) * float(valor2))
print("VALOR A PAGAR: R$ %0.2f" %apagar)
