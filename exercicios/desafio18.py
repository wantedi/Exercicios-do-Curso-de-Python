import math
num = int(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print(f'O valor do seno de {num} é: {sen:.2f}')
print(f'O valor do cosseno de {num} é: {cos:.2f}')
print(f'E o valor da tangente de {num} é: {tan:.2f}')
