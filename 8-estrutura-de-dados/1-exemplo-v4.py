from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    # Nome da variável: tipo de variável
    nome: str
    idade: int
    altura: float
    
lista_clientes = []

# SOLICITANDO DADOS DE UM CLIENTE.
for i in range(2):
    dados_do_cliente = Cliente(
        nome=input('Digite seu nome: '),
        idade=int(input('Digite sua idade: ')),
        altura=float(input('Digite sua altura: '))
    )
    lista_clientes.append(dados_do_cliente)

for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura}')
    print('='*15)