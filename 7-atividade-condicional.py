import os

# Limpa o terminal.
os.system('cls' if os.name == 'nt' else 'clear')

# ENTRADA.
numero = float(input("Digite um número: "))

# PROCESSAMENTO
if numero < 10:
    print("É MENOR QUE 10!")
else:
    print("É MAIOR QUE 10!")

# SAÍDA.
print('FIM DO PROGRAMA.')