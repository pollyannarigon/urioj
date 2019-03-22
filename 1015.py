from math import *

class Distancia():
    def calcula_distancia(self, x1, x2, y1, y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

        calculo_primeiro= (float(x2)-float(x1))**2
        #calculo_segundo= calculo_primeiro**2
        calculo_terceiro=(float(y2)-float(y1))**2
        #calculo_quarto=calculo_terceiro**2
        calculo_quinto= calculo_primeiro+calculo_terceiro
        final=sqrt(calculo_quinto)

        return print("%.4f" %final)


linha1=input().split(" ")
linha2=input().split(" ")
x1, y1 = linha1
x2, y2= linha2

teste=Distancia()
teste.calcula_distancia(x1,x2,y1,y2)
