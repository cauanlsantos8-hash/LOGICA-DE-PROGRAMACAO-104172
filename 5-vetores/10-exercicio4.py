import os
os.system('cls')


numeros = []

for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print("\n= NÚMEROS INFORMADOS =")
for i, num in enumerate(numeros, start=1):
    print(f"Número {i}: {num}")

print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")