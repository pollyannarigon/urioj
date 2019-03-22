tempo=int(input())

hora=int(tempo/3600)
minuto=int((tempo%3600)/60)
seg=int(tempo-(hora*3600)-(minuto*60))

print("%d:%d:%d" %(hora, minuto, seg))
