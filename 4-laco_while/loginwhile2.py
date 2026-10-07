import os
os.system('cls')

print('= TELA PARA CADASTRO =')
login_cadastrado = 'Cauan'
senha_cadastrada = '4002'

while True:
    os.system('cls')
    print('= TELA PARA LOGIN =')
    login_informado = input('Digite seu login: ')
    senha_informada = input('Digite sua senha: ')

    if login_informado == login_cadastrado and senha_informada == senha_cadastrada:
        print('Bem-vindo!')
        break
    else:
        print('Login ou senha incorretos. \nTente novamente! \n')
        input('Pressione uma tecla para continuar...')
