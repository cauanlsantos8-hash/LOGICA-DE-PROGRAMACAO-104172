import os
os.system('cls')

def verificar_positivo_negativo(numero):
    if numero < 0:
        resultado = 'negativo'
    else:
        resultado = 'positivo'
    return resultado

print('= Solicitando Dados =')
numero = int(input('Digite um número: '))

resultado = verificar_positivo_negativo(numero)