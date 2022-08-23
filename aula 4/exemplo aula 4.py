goiaba_kg = 8.00
caqui_kg = 12.00
morango_kg = 25.00

for i in range(3):
  valor = input()
  valor = float(valor)
  if valor <= 10.00:
    print('posso comprar!')
  else:
    print('não posso comprar!')
    