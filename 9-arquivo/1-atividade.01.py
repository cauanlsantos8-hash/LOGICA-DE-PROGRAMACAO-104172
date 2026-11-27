from dataclasses import dataclass
import os

os.system('cls')


@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str


ARQUIVO_CSV = 'dados_fornecedor.csv'
fornecedores_lidos = []

if os.path.exists(ARQUIVO_CSV):
    with open(ARQUIVO_CSV, 'r', encoding='utf-8') as arquivo_fornecedor:
        for linha in arquivo_fornecedor:
            linha = linha.strip()
            if not linha:
                continue

            partes = linha.split(',')
            if len(partes) == 4:
                nome, email, telefone, endereco = partes
                fornecedores_lidos.append(
                    Fornecedor(
                        nome=nome,
                        email=email,
                        telefone=telefone,
                        endereco=endereco,
                    )
                )

print('\nExibindo dados do fornecedor:')
for fornecedor in fornecedores_lidos:
    print(f'Nome: {fornecedor.nome}')
    print(f'E-mail: {fornecedor.email}')
    print(f'Telefone: {fornecedor.telefone}')
    print(f'Endereço: {fornecedor.endereco}')
    print('=========================')