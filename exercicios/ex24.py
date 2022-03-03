cid = str(input('Digite o nome da sua cidade: ')).strip()
div = cid.title().split()
print('Sua cidade começa com Santo?')
print('Santo' in div[0])
