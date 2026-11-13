import os

def limpar_tela():
    os.system('cls')
def logo_senai():
    print('===============')
    print(' SENAI - BAHIA')
    print('===============')

def exibir_menu():
    logo_senai()
    print('1 - Cadastrar Aluno')
    print('2 - Mostrar Dados Cadastrados.')
    print('0 - Sair')
    print('===============')

def cadastrar_pessoa():
    limpar_tela()
    logo_senai()
    print('\n--- Cadastro do Aluno ---')
    nome = input('Digite seu Nome: ')
    email = input('Digite seu E-Mail: ')
    telefone = input('Digite seu Telefone: ')

    print('\n Cadastro realizado com sucesso!')
    input('\nPressione ENTER para voltar ao menu...')

    return {'nome': nome, 'email': email, 'telefone': telefone}

def mostrar_dados(pessoa):
    limpar_tela()
    logo_senai()
    print('\n--- Dados Cadastrados ---')
    if pessoa:
        print(f'Nome: {pessoa['nome']}')
        print(f'E-Mail: {pessoa['email']}')
        print(f'Telefone: {pessoa['telefone']}')
    else:
        print('Nenhum cadastro encontrado no sistema!')
    print('=====================')
    input('\nPressione ENTER para voltar ao menu...')

def main():
    pessoa_cadastrada = None

    while True:
        limpar_tela()
        exibir_menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            pessoa_cadastrada = cadastrar_pessoa()
        elif opcao == '2':
            mostrar_dados(pessoa_cadastrada)
        elif opcao == '0':
            limpar_tela()
            logo_senai()
            print('\nSaindo do sistema... Até logo!')
            break
        else:
            print('\nOpção inválida!')
            input('Pressione ENTER para tentar novamente...')

if __name__ == '__main__':
    main()