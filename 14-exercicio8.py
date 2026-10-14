import os
os.system('cls')


numeros = []

for i in range(1, 6):
    valor_input = float(input(f"Digite o {i}º número: "))
    
    if valor_input < 0:
        numeros.append(0.0)
    else:
        numeros.append(valor_input)

print("\n= VALORES DO VETOR =")
for i, num in enumerate(numeros, start=1):
    print(f"Posição {i}: {num}")