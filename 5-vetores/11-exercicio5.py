import os
os.system('cls')


numeros = []
quantidade_pares = 0
quantidade_impares = 0

for i in range(1, 7):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(numero)
    
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

print("\n= NÚMEROS INFORMADOS =")
for i, numero in enumerate(numeros, start=1):
    print(f"{i}º Número: {numero}")

print(f"\nQuantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")