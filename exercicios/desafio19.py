import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lis = [n1, n2, n3, n4]
limp = random.choice(lis)
print(f'O aluno que irá limpar o quadro é: {limp}')
