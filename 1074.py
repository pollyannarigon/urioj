#4484 469,9
n=int(input())

for i in range (0, n, 1):
    entrada=int(input())
    if entrada == 0:
        print("NULL")
    else:
        if entrada%2==0 and entrada>0:
            print("EVEN POSITIVE")

        if entrada%2==0 and entrada<0:
            print("EVEN NEGATIVE")

        if entrada%2!=0 and entrada>0:
            print("ODD POSITIVE")

        if entrada%2!=0 and entrada<0:
            print("ODD NEGATIVE")
