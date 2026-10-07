import os
os.system('cls')


soma = 0
contador = 0

valor = int(input("Digite um número inteiro positivo (ou um negativo para parar): "))

while valor >= 0:
    soma += valor
    contador += 1
    valor = int(input("Digite o próximo número (ou um negativo para parar): "))

if contador > 0:
    media = soma / contador
    print(f"\nQuantidade de números informados: {contador}")
    print(f"A média aritmética é: {media:}")
else:
    print("\nNenhum número positivo foi digitado.")