dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados? '))
r = (dia * 60) + (km * 0.15)
print(f'O total a se pagar é de R${r}')
