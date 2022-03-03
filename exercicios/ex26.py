frase = str(input('Digite uma frase: ')).strip()
print('Sua frase tem', frase.lower().count('a'), 'letras A.')
print('A primeira letra A apareceu na posição:', frase.lower().find('a')+1)
print('A última letra A apareceu na posição:', frase.lower().rfind('a')+1)
