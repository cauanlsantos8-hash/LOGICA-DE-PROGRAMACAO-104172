import os
os.system('cls')

primeiro_numero = float(input('Digite o primeiro número: '))
segundo_numero = float(input('Digite o segundo número: '))

print('\nOs números informados foram:', primeiro_numero, 'e', segundo_numero)

if primeiro_numero > segundo_numero:
    print('O maior número é:', primeiro_numero)
    print('O menor número é:', segundo_numero)
elif segundo_numero > primeiro_numero:
    print('O maior número é:', segundo_numero)
    print('O menor número é:', primeiro_numero)
else:
    print('Os dois números são iguais.')
