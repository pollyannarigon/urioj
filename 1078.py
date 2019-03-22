#4390 473,9

class Tabuada():
    def calcula(self, multiplo):
        self.multiplo=multiplo

        for i in range (1, 11, 1):
            resultado=i*multiplo

            print("%d x %d = %d" %(i, entrada, resultado))


entrada=int(input())

teste=Tabuada()
teste.calcula(entrada)
