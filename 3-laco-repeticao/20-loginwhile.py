import os
os.system('cls')

login = "Cauan"
senha = "4002"


login = input("Digite o login: ")
senha = input("Digite a senha: ")


while login != login or senha != senha:
    print("Login ou senha incorretos. Tente novamente!\n")
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

print("Acesso permitido! Bem-vindo(a).")