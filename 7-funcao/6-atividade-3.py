import os
os.system('cls')

def gerar_tabuada(numero):
    print(f'\n--- Tabuada do {numero} ---')
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

def executar():
    num = int(input('Digite um número para ver a tabuada: '))
    gerar_tabuada(num)


executar()