import os

# limpa o terminal.
os.system("cls")

# SOLICITANDO DADOS.
#intput adicina o que for digitando no terminal na variável com texto.
nome = input('Digite seu nome: ')
sobrenome =input('Digite seu sobrenome: ')

# int() converte o que foi digitado em inteiro (números inteiros).
idade = int(input('Digite sua idade: '))

# float()converte o que foi digitado em float (números reais)
peso = float(input('Digite seu peso: '))
altura = float(input("Digite sua altura: "))

# MOSTRANDO DADOS.
print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('idade: ', idade)
print('peso: ', peso)
print('Altura: ', altura)
