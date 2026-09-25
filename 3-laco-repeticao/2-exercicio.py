import os
os.system('cls')

print('== TABUADA ==')
numero = int(input('Digite um número: '))

for i in range(1, 11):
# ADIÇÃO.
    print(f'{numero} + {i} = {numero + i} ')

# SUBTRAIR.
    print(f'{numero} - {i} = {numero - i} ')

# MULTIPLICAR.
    print(f'{numero} x {i} = {numero * i} ')

# DIVIDIR.
    print(f'{numero} / {i} = {numero / i} ')



    print('== FIM DO PROGRAMA ==')