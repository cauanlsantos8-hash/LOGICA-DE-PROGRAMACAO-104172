import os
os.system('cls')

def inflacionar_preco(preco):
    if preco < 100:
        return preco * 1.10
    else:
        return preco * 1.20

print('= Solicitando Dados =')
preco_original = float(input('Digite o preço do produto: R$ '))

print('= Exibindo Dados =')
novo_preco = inflacionar_preco(preco_original)
print(f'O novo preço inflacionado é: R$ {novo_preco}')