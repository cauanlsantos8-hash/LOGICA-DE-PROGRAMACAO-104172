import os
os.system('cls')


numeros = []
quantidade_negativos = 0
soma_positivos = 0.0

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)
    
    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        soma_positivos += numero

print("\n=== RESULTADOS ===")
print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")