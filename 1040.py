'''
entrada=input().split(" ")
n1=float(entrada[0])
n2=float(entrada[1])
n3=float(entrada[2])
n4=float(entrada[3])

media1=float(((n1*2)+(n2*3)+(n3*4)+(n4*1))/10)
print("Media: %0.1f" %media1)

if media1 >= 7.0:
    print("Aluno aprovado.")

elif media1 < 5.0:
    print("Aluno reprovado.")

elif media1 > 5.0 and  media1<=6.9:
    print("Aluno em exame.")
    exame=float(input(''))
    print('Nota do exame: {:.1f}'.format(exame))

    novanota=float((media1 + exame)/2.0)

    if novanota >= 5.0:

        print("Aluno aprovado.")

    elif novanota <= 4.9:

        print("Aluno reprovado.")

    print("Media final: %0.1f" %novanota)
'''


#cod correto:
ns = (input('')).split()
a = float(ns[0])
b = float(ns[1])
c = float(ns[2])
d = float(ns[3])
m = ((a * 2) + (b * 3) + (c * 4) + (d)) / 10
print('Media: {:.1f}'.format(m))
if m >= 7.0:
    print('Aluno aprovado.')
elif m < 5.0:
    print('Aluno reprovado.')
elif m >= 5.0 and m <= 6.9:
    print('Aluno em exame.')
    ne = float(input(''))
    print('Nota do exame: {:.1f}'.format(ne))
    m = (ne + m) / 2
    if m >= 5.0:
        print('Aluno aprovado.')
    elif m <= 4.9:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(m))
