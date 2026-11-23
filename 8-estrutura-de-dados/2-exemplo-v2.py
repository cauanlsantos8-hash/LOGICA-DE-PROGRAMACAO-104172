from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str

    # Função dentro da classe.
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'E-Mail: {self.email}')
        print('='*30)

    # Função somente para enviar e-mails.
    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'E-Mail: {self.email}')
        print('='*30)

    # Função somente para enviar Whatszapp.
    def whatsapp_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*30)

dados_cliente = []

for i in range(2):
    dados_do_cliente = Cliente(
        nome=input('Digite seu nome: '),
        telefone=input('Digite seu telefone: '),
        email=input('Digite seu E-Mail: ')
    )
    dados_cliente.append(dados_do_cliente)

print('\n= Exibindo Todos os Dados =')
for cliente in dados_cliente:
    cliente.mostrar_dados()

print('\n= Exibindo E-Mail Marketing =')
for cliente in dados_cliente:
    cliente.email_marketing()

print('\n= Exibindo WhatsApp Marketing =')
for cliente in dados_cliente:
    cliente.whatsapp_marketing()