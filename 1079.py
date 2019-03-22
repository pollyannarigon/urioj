cs=int(input())

for i in range(0, cs, 1):
    notas=input().split(" ")
    n1=float(notas[0])*2
    n2=float(notas[1])*3
    n3=float(notas[2])*5
    media=(n1+n2+n3)/10
    print("%0.1f" %media)
