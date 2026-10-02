import os
import time
os.system('cls')

# MATENDO OS DADOS.
login_salvo = 'Cauan'
senha_salva ='@4002'

while True:
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')

    if login == login_salvo and senha == senha_salva:
        print('Bem vindo!')
        break
    else:
        print('\nLogin ou senha inválida.')
        print('Tente novamente! \n')
        input('Pressione uma tecla pra continuar...')
        os.system('cls')


print('= FIM. =')