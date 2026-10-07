import os
os.system('cls')

login_salvo = 'Cauan'
senha_salva = '4002'
tentativas = 1

while True:
    if tentativas <= 3:
        print(f'Tentativa: {tentativas} ')
        login = input('Digite o login: ')
        senha = input('Digite a senha: ')
        tentativas += 1

        if login == login and senha == senha_salva:
            print('Bem vindo!')
            break
        else:
            print('\nLogin ou senha inválida.')
            print('Tente novamente! \n')
            input('Pressione uma tecla para continuar...')
            os.system('cls')
    else:
        print('= FIM =')
        break


    