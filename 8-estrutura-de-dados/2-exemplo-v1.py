from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str

dados_cliente = []

for i in range(2):
    dados_do_cliente = Cliente(
        nome=input('Digite seu nome: '),
        telefone=input('Digite seu telefone: '),
        email=input('Digite seu E-Mail: ')
    )
    dados_cliente.append(dados_do_cliente)

print('\n = Exibindo Dados =')
for cliente in dados_cliente:
    print(f'Nome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'E-Mail: {cliente.email}')