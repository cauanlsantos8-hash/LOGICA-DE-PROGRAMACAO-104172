import os
import time

soma = 0
quantidade_numeros = 0

while True:
    os.system('cls')
    numero = int(input('Digite um número: '))

    if numero >= 0:
        soma += numero
        quantidade_numeros += 1
        time.sleep(2)
    else:
        break

if quantidade_numeros == 0:
    print('Não foram inseridos números. \n')
else:
    media = soma / quantidade_numeros
    print(f'Média: {media}')