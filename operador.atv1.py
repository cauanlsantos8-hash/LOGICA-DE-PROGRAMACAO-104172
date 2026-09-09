import os
os.system('cls')

# ENTRADA.
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

# PROCESSAMENTO.
valido = True
match operador:
    case '+':
        resultado = primeiro_numero + segundo_numero
    case '-':
        resultado = primeiro_numero - segundo_numero
    case '*':
        resultado = primeiro_numero * segundo_numero
    case '/':
        if segundo_numero != 0:
            resultado = primeiro_numero / segundo_numero
        else:
            resultado = "Erro! Não é possível dividir por zero."
            valido = False
    case _:
        resultado = "Operador inválido!"
        valido = False

# SAÍDA.
print("\n= RESUMO DA OPERAÇÃO =")
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {primeiro_numero}")
print(f"Operador escolhido: {operador}")

if valido:
    print(f"Resultado: {resultado:.2f}")
else:
    print(f"Resultado: {resultado}")