a = input('Digite algo: ')
print(f'Qual seu tipo primitivo? {type(a)}')
print(f'É alfabético? {a.isalpha()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfanúmerico? {a.isalnum()}')
print(f'Está todo em minúsculas? {a.islower()}')
print(f'Está todo em maiúsculas? {a.isupper()}')
print(f'É um espaço? {a.isspace()}')
print(f'Está capitalizado? {a.istitle()}')
