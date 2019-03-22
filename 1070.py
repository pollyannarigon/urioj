#4554 464,1
entrada=int(input())
if entrada%2==0:
    entrada=entrada+1
for i in range(entrada, entrada+12, 2):
    print(i)
