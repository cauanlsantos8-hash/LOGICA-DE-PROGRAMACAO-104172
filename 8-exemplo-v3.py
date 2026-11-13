import os


# Função sem retorno e sem parâmetros
def logo_senai():
    os.system('cls')
    print('=========')
    print('  SENAI')
    print('=========')

    # Função sem retorno e com parâmetros.
    def mostrar_dados(nome, idade):
        print(f'{nome} tem {idade} anos.')

    # Função sem retorno e sem parâmentros.
    logo_senai()
    print('\n= Solicitando dados =')
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
