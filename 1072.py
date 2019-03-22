n=int(input())
numin=0
numout=0

for i in range(0, n, 1):
    ni=int(input())
    if ni >=10 and ni<=20:
        numin=numin+1
    else:
        numout=numout+1


print("%d in" %numin)
print("%d out" %numout)
