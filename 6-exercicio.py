import os
os.system('cls')

soma = 0

for i in range(3):
    numero = int(input('Digite um número: '))
    soma = numero + soma

print(f'Soma: {soma}')

print('Fim.')