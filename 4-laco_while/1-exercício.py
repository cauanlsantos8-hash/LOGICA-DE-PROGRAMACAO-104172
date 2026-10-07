import os

def limpar_tela():
    os.system('cls')

total_conta = 0.0
continuar = "S"

while continuar.upper() == "S":
    limpar_tela()
    print("=== CARDÁPIO DO RESTAURANTE ===")
    print("1 - Prato Feito ----- R$ 25.00")
    print("2 - Strogonoff de Frango - R$ 30.00")
    print("3 - Lasanha à Parmegiana - R$ 35.00")
    print("4 - Salada-X -------- R$ 20.00")
    print("5 - Suco Natural --------- R$  8.00")
    
    try:
        opcao = int(input("Escolha o número do prato desejado: "))
    except ValueError:
        opcao = 0

    if opcao == 1:
        total_conta += 25.00
        print("\nItem adicionado: Prato Feito (R$ 25,00)")
    elif opcao == 2:
        total_conta += 30.00
        print("\nItem adicionado: Strogonoff de Frango (R$ 30,00)")
    elif opcao == 3:
        total_conta += 35.00
        print("\nItem adicionado: Lasanha à Parmegiana (R$ 35,00)")
    elif opcao == 4:
        total_conta += 20.00
        print("\nItem adicionado: Salada-X (R$ 20,00)")
    elif opcao == 5:
        total_conta += 8.00
        print("\nItem adicionado: Suco Natural (R$ 8,00)")
    else:
        print("\nOpção inválida! Nenhum item foi adicionado.")

    continuar = input("\nDeseja escolher outro prato? (S/N): ").strip()

limpar_tela()
print("=== CONTA FINAL ===")
print(f"Total a pagar pelo cliente: R$ {total_conta:}")