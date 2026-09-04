import os
os.system('cls')

# ENTRADA.
login = input('Digite o login: ')
senha = input('Digite a senha: ')

# PROCESSAMENTO.
login_salvo = 'Cauan'
senha_salva = '12345678'

# SAÍDA.
if login == login_salvo and senha == senha_salva:
    print('Bem-vindo!')
else:
    print('Login ou senha inválida.')
