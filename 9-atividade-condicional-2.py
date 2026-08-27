import os

# Limpa o terminal
os.system("cls")

# ENTRADA
print("= ANÁLISE DE DOIS NÚMEROS =")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# PROCESSAMENTO MATEMÁTICO
soma = num1 + num2
media = soma / 2
produto = num1 * num2

# PROCESSAMENTO LÓGICO.
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

# SAÍDA.
print("\n= RESULTADOS =")
print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto (Multiplicação): {produto}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")




