import math
class Maior():
    def compara(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

        maior=(int(a) + int(b) + abs(int(a) - int(b)))  / 2
        result= (int(maior) + int(c) + abs(int(maior) - int(c)))/2
        return print("%d eh o maior" %result)

entrada=input().split(" ")
a_in, b_in, c_in = entrada

teste=Maior()
teste.compara(a_in,b_in, c_in)
