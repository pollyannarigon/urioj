class CalculaIR():
    def calculo(self, salario):
        self.salario=salario

        if salario <= 2000:
            print("Isento")
        #calculo de 8% em cima do sal[ario ]
        if salario >2000 and salario <= 3000:
            ir=(salario-2000)*0.08
            return print("R$ %0.2f" %ir)
        #calculo de 18%
        if salario >3000 and salario <=4500:
            diferenca1= salario -2000 #isento
            diferenca2= 1000*0.08
            diferenca3=salario-3000
            ir=(diferenca3*0.18)+diferenca2
            return print("R$ %0.2f" %ir)

        if salario >4500:
            diferenca1= salario -2000 #isento
            diferenca2= 1000*0.08
            diferenca3=1500*0.18
            diferenca4=salario-4500
            diferenca5=diferenca4*0.28
            ir=diferenca5+diferenca3+diferenca2
            return print("R$ %0.2f" %ir)





entrada=float(input())
calcular=CalculaIR()
calcular.calculo(entrada)
