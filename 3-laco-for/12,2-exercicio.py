import os
os.system('cls')


print('ACUMULANDO VALORES EM VARIÁVEL.')
soma = 0

for i in range(3):
    soma += int(input('Digite um número para somar: '))


print(f'\nValor FINAL da variável soma: {soma}')