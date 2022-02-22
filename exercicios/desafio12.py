p = int(input('Digite o preço do produto? R$:'))
d = int(input('Digite o desconto:'))
r = p*d/100
print(f'O produto que valia {p} com o desconto de {d} agora vale R${p-r:.2f}')
