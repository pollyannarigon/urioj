

class CalculaPositivos():
    def calculo(self, numero):
        self.numero=numero
        count=0

        for i in range (0, 6, 1):
            if numero[i] >0:
                count=count+1

        return print("%d valores positivos\ %count)




n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())
n6=float(input())

nums=[]
nums.append(n1)
nums.append(n2)
nums.append(n3)
nums.append(n4)
nums.append(n5)
nums.append(n6)



numeros=CalculaPositivos()
numeros.calculo(nums)
