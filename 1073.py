from math import *
entrada=int(input())
if entrada >5 and entrada <20000:


    for i in range(2, entrada+1, 2):
        saida=int(pow(i,2))
        print("%d^%d = %d"%(i,2,saida))
