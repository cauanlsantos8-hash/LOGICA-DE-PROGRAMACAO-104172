import os
os.system('cls')

# Constante.
QUANTIDADE_REPETICOES = 5
pares = 0
impares = 0


for i in range(QUANTIDADE_REPETICOES):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares = pares + 1
        pares += 1
    else:
        impares += 1

print(f'Quantidade de pares: {pares}')
print(f'Quantidade de impares: {impares}')

print('Fim.')