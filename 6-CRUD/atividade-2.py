import os

lista_pacientes = []

while True:
    os.system('cls')
    print('''
== CADASTRO DE PACIENTES - HOSPITAL ==
1 - Cadastrar paciente
2 - Listar todos os pacientes
3 - Atualizar paciente
4 - Remover paciente
5 - Buscar paciente
0 - Sair
''')
    
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Opção inválida! Digite apenas números.')
        input('\nPressione Enter para continuar...')
        continue

    match opcao:
        case 1:
            # CREATE (INSERIR)
            print('\n== CADASTRAR PACIENTE ==')
            nome = input('Nome: ').strip()
            sobrenome = input('Sobrenome: ').strip()

            if nome == '' or sobrenome == '':
                print('Erro: Nome e sobrenome não podem ser vazios!')
            else:
                lista_pacientes.append({'nome': nome, 'sobrenome': sobrenome})
                print('Paciente cadastrado com sucesso!')

        case 2:
            # READ (LISTAR TODOS)
            print('\n== LISTA DE PACIENTES ==')
            if len(lista_pacientes) == 0:
                print('Nenhum paciente cadastrado.')
            else:
                for i, paciente in enumerate(lista_pacientes, start=1):
                    print(f'{i}. {paciente["nome"]} {paciente["sobrenome"]}')
                print(f'\nTotal: {len(lista_pacientes)} paciente(s)')

        case 3:
            # UPDATE (ATUALIZAR)
            print('\n== ATUALIZAR PACIENTE ==')
            if len(lista_pacientes) == 0:
                print('Nenhum paciente cadastrado.')
            else:
                for i, paciente in enumerate(lista_pacientes, start=1):
                    print(f'{i}. {paciente["nome"]} {paciente["sobrenome"]}')

                try:
                    num = int(input('\nDigite o número do paciente para atualizar: '))
                    if 1 <= num <= len(lista_pacientes):
                        novo_nome = input('Novo Nome: ').strip()
                        novo_sobrenome = input('Novo Sobrenome: ').strip()

                        if novo_nome == '' or novo_sobrenome == '':
                            print('Erro: O novo nome e sobrenome não podem ser vazios!')
                        else:
                            lista_pacientes[num - 1]['nome'] = novo_nome
                            lista_pacientes[num - 1]['sobrenome'] = novo_sobrenome
                            print('Paciente atualizado com sucesso!')
                    else:
                        print('Número de paciente inexistente!')
                except ValueError:
                    print('Digite um número válido!')

        case 4:
            # DELETE (REMOVER)
            print('\n== REMOVER PACIENTE ==')
            if len(lista_pacientes) == 0:
                print('Nenhum paciente cadastrado.')
            else:
                for i, paciente in enumerate(lista_pacientes, start=1):
                    print(f'{i}. {paciente["nome"]} {paciente["sobrenome"]}')

                try:
                    num = int(input('\nDigite o número do paciente para remover: '))
                    if 1 <= num <= len(lista_pacientes):
                        removido = lista_pacientes.pop(num - 1)
                        print(f'Paciente {removido["nome"]} {removido["sobrenome"]} removido com sucesso!')
                    else:
                        print('Número de paciente inexistente!')
                except ValueError:
                    print('Digite um número válido!')

        case 5:
            # CRUD (BUSCAR)
            print('\n== BUSCAR PACIENTE ==')
            if len(lista_pacientes) == 0:
                print('Nenhum paciente cadastrado.')
            else:
                termo = input('Digite o nome ou sobrenome para buscar: ').strip().lower()
                if termo == '':
                    print('O termo de busca não pode ser vazio!')
                else:
                    encontrado = False
                    for i, paciente in enumerate(lista_pacientes, start=1):
                        if termo in paciente['nome'].lower() or termo in paciente['sobrenome'].lower():
                            print(f'{i}. {paciente["nome"]} {paciente["sobrenome"]}')
                            encontrado = True
                    
                    if not encontrado:
                        print('Nenhum paciente encontrado com esse termo.')

        case 0:
            print('Saindo do programa...')
            break

        case _:
            print('Opção inválida!\nTente novamente...')

    input('\nPressione Enter para continuar...')