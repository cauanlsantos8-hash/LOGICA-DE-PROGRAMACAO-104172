import os
os.system('cls')

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))
terceiro_numero = float(input('Digite o terceiro número: '))

maior = max(primeiro_numero, segundo_numero, terceiro_numero)
menor = min(primeiro_numero, segundo_numero, terceiro_numero)

print(f'\nPrimeiro número: {primeiro_numero}')
print(f'Segundo número: {segundo_numero}')
print(f'Terceiro número: {terceiro_numero}')
print(f'Maior número: {maior}')
print('Menor número: {menor}')

