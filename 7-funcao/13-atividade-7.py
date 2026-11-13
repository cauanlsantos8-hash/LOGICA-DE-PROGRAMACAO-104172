import os
os.system('cls')

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não permitida"
    return a / b

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\n--- Resultados ---")
print("Soma:", somar(n1, n2))
print("Subtração:", subtrair(n1, n2))
print("Multiplicação:", multiplicar(n1, n2))
print("Divisão:", dividir(n1, n2))