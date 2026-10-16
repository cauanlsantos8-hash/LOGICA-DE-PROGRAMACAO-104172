import os
os.system('cls')


numeros = []

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print("\n= NÚMEROS INFORMADOS =")
for i, numero in enumerate(numeros, start=1):
    print(f"Número {i}: {numero}")

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")