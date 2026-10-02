import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIÁVEL.')
soma = 0

print(f'\nValor INICIAL da variável soma: {soma}')


for i in range(3):
    numero = int(input('Digite um número para somar: '))
    soma = soma + numero
    print(f'\nValor TEMPORÁRIO da variável soma: {soma}')

print(f'\nValor FINAL da variável soma: {soma}')





