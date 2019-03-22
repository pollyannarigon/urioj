class Gasto():
    def calcula_gasto(self, distancia, tempo):
        self.distancia=distancia
        self.tempo=tempo

        return print("%0.3f" %((self.distancia*self.tempo)/12))

in_dist=int(input())
in_temp=int(input())

calc=Gasto()
calc.calcula_gasto(in_dist,in_temp)
