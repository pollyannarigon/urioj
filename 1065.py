#4645 461,6
class CalculaPares():
    def calculo(self, numero):
        self.numero=numero
        count=0

        for i in range (0, 5, 1):
            if numero[i]%2==0:
                count=count+1


        return print("%d valor(es) par(es)" %count)

class CalculaImpares():
    def calculo(self, numero):
        self.numero=numero
        count=0

        for i in range (0, 5, 1):
            if numero[i]%2!=0:
                count=count+1


        return print("%d valor(es) impar(es)" %count)


class CalculaPositivos():
    def calculo(self, numero):
        self.numero=numero
        count=0

        for i in range (0, 5, 1):
            if numero[i] >0:
                count=count+1

        return print("%d valor(es) positivo(s)" %count)



class CalculaNegativos():
    def calculo(self, numero):
        self.numero=numero
        count=0

        for i in range (0, 5, 1):
            if numero[i] < 0:
                count=count+1

        return print("%d valor(es) negativo(s)" %count)






n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())


nums=[]
nums.append(n1)
nums.append(n2)
nums.append(n3)
nums.append(n4)
nums.append(n5)




numeros=CalculaPares()
numeros.calculo(nums)
numeros=CalculaImpares()
numeros.calculo(nums)
numeros=CalculaPositivos()
numeros.calculo(nums)
numeros=CalculaNegativos()
numeros.calculo(nums)
