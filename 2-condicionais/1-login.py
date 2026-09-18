import os
os.system('cls')

# ENTRADA.
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# PROCESSAMENTO.
if login == "Cauan" and senha == "12345678":
    print("Bem-vindo!")

# SÁIDA.
else:
    print("Login ou senha inválido.")
