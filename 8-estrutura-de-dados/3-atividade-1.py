from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome: str
    idade: float
    telefone: str
    endereco: str

    # Função dentro da classe.
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')
        print('='*30)

    # Função somente para enviar e-mails.
    def idade_paciente(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print('='*30)

    # Função somente para enviar Whatszapp.
    def telefone_paciente(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*30)
    
dados_cliente = []

for i in range(1):
    print('\n= Dados do Paciente =')
    dados_do_cliente = Cliente(
        nome=input('Digite seu nome: '),
        idade=float(input('Digite sua idade: ')),
        telefone=input('Digite seu telefone: '),
        endereco=input('Digite seu endereço: ')
    )
    dados_cliente.append(dados_do_cliente)

print('\n = Dados do Paciente =')
for cliente in dados_cliente:
    cliente.mostrar_dados()

    print('\n= Exibindo Idade do Paciente =')
for cliente in dados_cliente:
    cliente.idade_paciente()

print('\n= Exibindo Telefone do Paciente =')
for cliente in dados_cliente:
    cliente.telefone_paciente()