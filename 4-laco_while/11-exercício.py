import os
os.system('cls')


numeros = 0
impares = 0
pares = 0
soma_geral = 0
total_numeros = 0

numero = int(input("Digite um número inteiro positivo (ou 0 para encerrar): "))

while numero != 0:
    soma_geral += numero
    total_numeros += 1

    if numero % 2 == 0:
        pares += 1
        pares += numero
    else:
        impares += 1

    numero = int(input("Digite o próximo número (ou 0 para encerrar): "))

print("\n= RESULTADOS =")
if total_numeros > 0:
    media_geral = soma_geral / total_numeros

    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

    if pares > 0:
        media_pares = pares / pares
        print(f"Média dos valores pares: {pares:}")
    else:
        print("Média dos valores pares: Nenhum número par foi inserido.")

    print(f"Média geral dos números lidos: {media_geral:}")
else:
    print("Nenhum número foi digitado.")