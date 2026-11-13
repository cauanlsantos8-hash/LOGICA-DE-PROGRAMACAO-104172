import os
os.system('cls')

def logo_senai():
    print('===============')
    print(' SENAI - BAHIA ')
    print('===============')

def mostrar_dados(nome, email, telefone):
    logo_senai()
    print('\n --- DADOS CADASTRADOS ---')
    print(f'Nome: {nome}')
    print(f'E-Mail: {email}')
    print(f'Telefone: {telefone}')
    print('===============')

logo_senai()

nome = input('Digite seu Nome: ')
email = input('Digite seu E-Mail: ')
telefone = input('Digite seu Telefone: ')

mostrar_dados(nome, email, telefone)