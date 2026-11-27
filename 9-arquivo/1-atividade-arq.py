from dataclasses import dataclass
import os

os.system('cls')


@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str


QUANTIDADE_FORNECEDOR = 2
ARQUIVO_CSV = 'dados_fornecedor.csv'

lista_fornecedor = []

for _ in range(QUANTIDADE_FORNECEDOR):
    novo_fornecedor = Fornecedor(
        nome=input('Digite seu nome: ').strip(),
        email=input('Digite seu e-mail: ').strip(),
        telefone=input('Digite seu telefone: ').strip(),
        endereco=input('Digite seu endereço: ').strip(),
    )
    lista_fornecedor.append(novo_fornecedor)

with open(ARQUIVO_CSV, 'a', encoding='utf-8') as arquivo_fornecedor:
    for fornecedor in lista_fornecedor:
        arquivo_fornecedor.write(
            f'{fornecedor.nome},{fornecedor.email},{fornecedor.telefone},{fornecedor.endereco}\n'
        )

print('\nFornecedor salvo com sucesso!')