import os



def limpar_tela():
    os.system('cls')

pratos_escolhidos = []
precos_escolhidos = []

continuar = "S"

while continuar.upper() == "S":
    limpar_tela()
    print("= CARDÁPIO DO RESTAURANTE =")
    print("1 - Prato Feito ---------- R$ 25.00")
    print("2 - Strogonoff de Frango - R$ 30.00")
    print("3 - Lasanha Mista -------- R$ 35.00")
    print("4 - Salada Saudável ------ R$ 20.00")
    print("5 - Suco Natural --------- R$  8.00")
    
    try:
        opcao = int(input("Escolha o número do prato desejado: "))
    except ValueError:
        opcao = 0

    if opcao == 1:
        pratos_escolhidos.append("Prato Feito")
        precos_escolhidos.append(25.00)
        print("\nItem adicionado com sucesso!")
    elif opcao == 2:
        pratos_escolhidos.append("Strogonoff de Frango")
        precos_escolhidos.append(30.00)
        print("\nItem adicionado com sucesso!")
    elif opcao == 3:
        pratos_escolhidos.append("Lasanha Mista")
        precos_escolhidos.append(35.00)
        print("\nItem adicionado com sucesso!")
    elif opcao == 4:
        pratos_escolhidos.append("Salada Saudável")
        precos_escolhidos.append(20.00)
        print("\nItem adicionado com sucesso!")
    elif opcao == 5:
        pratos_escolhidos.append("Suco Natural")
        precos_escolhidos.append(8.00)
        print("\nItem adicionado com sucesso!")
    else:
        print("\nOpção inválida! Nenhum item foi adicionado.")

    continuar = input("\nDeseja escolher outro prato? (S/N): ").strip()

limpar_tela()
print("= RESUMO DO PEDIDO =")
if pratos_escolhidos:
    for i in range(len(pratos_escolhidos)):
        print(f"{i + 1}. {pratos_escolhidos[i]} - R$ {precos_escolhidos[i]}")
    
    total_conta = sum(precos_escolhidos)
    print("-" * 35)
    print(f"Total a pagar pelo cliente: R$ {total_conta}")
else:
    print("Nenhum pedido foi realizado.")