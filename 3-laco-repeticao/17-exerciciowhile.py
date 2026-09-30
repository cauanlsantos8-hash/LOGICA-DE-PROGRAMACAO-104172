import os
os.system('cls')

while True:
    numero = int(input('Informe uma nota entre 1 e 10: '))
    if numero < 0 or numero > 10:
        print()
        print('Nota inválida, tente novamente!')
    else:
        print()
        print('A nota está entre 0 e 10.')
        break

print('= FIM =')