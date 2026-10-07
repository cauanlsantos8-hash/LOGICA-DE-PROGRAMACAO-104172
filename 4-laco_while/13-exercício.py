import os
def limpar_tela():
    os.system('cls')


total_familias = 0
soma_salarios = 0.0
soma_filhos = 0
maior_salario = None
menor_salario = None

opcao = 0

while opcao != 2:
    print("= MENU DE OPÇÕES =")
    print("1 - Adicionar família")
    print("2 - Sair e exibir resultados")
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        limpar_tela()
        print("Entrada inválida! Digite um número do menu.\n")
        continue

    if opcao == 1:
        limpar_tela()
        print("= CADASTRAR FAMÍLIA =")
        salario = float(input("Digite o salário da família (R$): "))
        filhos = int(input("Digite o número de filhos: "))

        soma_salarios += salario
        soma_filhos += filhos
        total_familias += 1

        if maior_salario is None or salario > maior_salario:
            maior_salario = salario
        if menor_salario is None or salario < menor_salario:
            menor_salario = salario

        limpar_tela()
        print("Família adicionada com sucesso!\n")

    elif opcao == 2:
        limpar_tela()
        print("= RESULTADOS DA PESQUISA =")
        if total_familias > 0:
            media_salario = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias

            print(f"a) Total de famílias que responderam a pesquisa: {total_familias}")
            print(f"b) Média do salário da população: R$ {media_salario:}")
            print(f"c) Média do número de filhos: {media_filhos:}")
            print(f"d) Maior salário: R$ {maior_salario:}")
            print(f"e) Menor salário: R$ {menor_salario:}")
        else:
            print("Nenhuma família foi cadastrada.")
        print()
    else:
        limpar_tela()
        print("Opção inválida! Tente novamente.\n")


