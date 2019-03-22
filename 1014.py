class Consumo():
    def calcula_consumo(self, distancia, combustivel):
        self.distancia=distancia
        self.combustivel=combustivel
        consumo=self.distancia/self.combustivel

        return print("%0.3f km/l" %consumo)

dis=int(input())
comb=float(input())

teste=Consumo()
teste.calcula_consumo(dis, comb)
