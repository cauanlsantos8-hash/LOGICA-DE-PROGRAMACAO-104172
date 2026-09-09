import os

os.system('cls')

# ENTRADA.
valor_produto = float(input("Digite o valor do produto (R$): "))

print("\n=== FORMAS DE PAGAMENTO ===")
print("1 - Pagamento à vista (10% de desconto)")
print("2 - Pagamento à prazo (Até 6x)")
opcao = int(input("Escolha a opção (1 ou 2): "))

# PROCESSAMENTO.
match opcao:
    case 1:
        desconto = valor_produto * 0.10
        total = valor_produto - desconto

        print("\nValor do produto: R$", f"{valor_produto:.2f}")
        print("Forma de pagamento: à vista")
        print("Valor do desconto: R$", f"{desconto:.2f}")
        print("Total a pagar: R$", f"{total:.2f}")

    case 2:
        parcelas = int(input("Digite a quantidade de parcelas (1 a 6): "))

        if 1 <= parcelas <= 6:
            valor_parcela = valor_produto / parcelas

            print("\nValor do produto: R$", f"{valor_produto:.2f}")
            print("Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print("Valor por parcela: R$", f"{valor_parcela:.2f}")
            print("Total à prazo: R$", f"{valor_produto:.2f}")
        else:
            print("\nQuantidade de parcelas inválida! Escolha entre 1 e 6 parcelas.")

# SAÍDA.
    case _:
        print("\nOpção de pagamento inválida!")