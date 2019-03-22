#4507 466,3
x=int(input())
y=int(input())

if x%2==0:
    x=x-1
else:
    x=x-2
count=0
soma=count

for i in range (x, y, -2):
    soma=soma+i


print(soma)
