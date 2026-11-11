import os
os.system('cls')

# Criando uma função.
def cabecalho():
    print('\n')
    print('='*15)
    print('      SENAI')
    print('='*15)

    cabecalho() #Usando a função.
    nome = input('Digite seu nome: ')

    cabecalho() # Usando a função.
    idade = input('Digite sua idade: ')

    cabecalho() # Usando a função.
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')