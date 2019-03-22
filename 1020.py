class Idade():
    def calculo(self, dias):
        self.dias=dias

        print("%d ano(s)" %(self.dias/365))
        print("%d mes(es)" %((self.dias%365)/30))
        contador=self.dias
        contador= contador - int(self.dias/365)*365
        contador=contador - int((self.dias%365)/30)*30
        print("%d dia(s)" %contador)




entrada=int(input())
pessoa=Idade()
pessoa.calculo(entrada)
