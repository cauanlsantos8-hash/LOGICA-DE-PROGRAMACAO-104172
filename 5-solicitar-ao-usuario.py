import os
os.system('cls')

# ENTRADA.
nota = float(input("Digite uma nota: "))

# PROCESSAMENTO.
if 0 <= nota <= 10:
    print(f"Nota informada: {nota}")

# SAÍDA.
else:
    print("A nota deve ser entre zero e dez.")