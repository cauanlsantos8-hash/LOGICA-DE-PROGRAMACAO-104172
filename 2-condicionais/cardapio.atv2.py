import os

os.system('cls' if os.name == 'nt' else 'clear')

# EXIBIÇÃO DO CARDÁPIO.
print("=== CARDÁPIO DO RESTAURANTE ===")
print("1 - Picanha na Chapa    - R$ 50.00")
print("2 - Lasanha à Bolonhesa  - R$ 35.00")
print("3 - Strogonoff de Frango - R$ 30.00")
print("4 - Salada Caesar       - R$ 20.00")
print("===============================")

# ENTRADA.
codigo = int(input("\nDigite o código do prato desejado: "))

# PROCESSAMENTO E SAÍDA.
match codigo:
    case 1:
        print("\nPrato escolhido: Picanha na Chapa")
        print("Valor: R$ 50.00")
    case 2:
        print("\nPrato escolhido: Lasanha à Bolonhesa")
        print("Valor: R$ 35.00")
    case 3:
        print("\nPrato escolhido: Strogonoff de Frango")
        print("Valor: R$ 30.00")
    case 4:
        print("\nPrato escolhido: Salada Caesar")
        print("Valor: R$ 20.00")
    case _:
        print("\nCódigo inválido! Por favor, escolha uma opção válida do cardápio.")