import os
def limpar_tela():
    os.system('cls')


total_pessoas = 0
soma_salarios = 0.0
maior_idade = 0
menor_idade = 0
quantidade_mulheres_5k = 0

opcao = 0

while opcao != 3:
    print("= MENU DE OPÇÕES =")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        limpar_tela()
        print("Entrada inválida! Digite um número do menu.\n")
        continue

    if opcao == 1:
        limpar_tela()
        print("= CADASTRAR PESSOA =")
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").strip().upper()
        salario = float(input("Digite o salário (R$): "))

        soma_salarios += salario
        total_pessoas += 1

        if maior_idade or  idade > maior_idade:
            maior_idade = idade
        if menor_idade or idade < menor_idade:
            menor_idade = idade

        if sexo == 'F' and salario >= 5000.0:
        
            quantidade_mulheres_5k += 1

        limpar_tela()
        print("Pessoa adicionada com sucesso!\n")

    elif opcao == 2:
        limpar_tela()
        print("= RESULTADOS DA PESQUISA =")
        if total_pessoas > 0:
            media_salario = soma_salarios / total_pessoas
            print(f"a) Média de salário do grupo: R$ {media_salario:}")
            print(f"b) Maior idade: {maior_idade} ano(s) | Menor idade: {menor_idade} ano(s)")
            print(f"c) Mulheres com salário a partir de R$ 5.000,00: {quantidade_mulheres_5k}")
        else:
            print("Nenhum dado foi cadastrado ainda.")
        print()

    elif opcao == 3:
        print("Encerrando o programa...")
    else:
        limpar_tela()
        print("Opção inválida! Tente novamente.\n")