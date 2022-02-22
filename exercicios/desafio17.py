from math import hypot
opos = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(opos, adj)
print(f'O valor da hypotenusa é: {hi:.2f}')
