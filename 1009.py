nome=input()
sal_fixo=float(input())
vendas=float(input())

bonus=float((vendas*0.15)+sal_fixo)

print("TOTAL = R$ %0.2f" %bonus)
