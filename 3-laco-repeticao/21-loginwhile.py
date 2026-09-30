import os
os.system('cls')

LOGIN_CORRETO = "Cauan"
SENHA_CORRETA = "4002"
LIMITE_TENTATIVAS = 3

tentativas = 0
autenticado = False

while tentativas < LIMITE_TENTATIVAS:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    
    if login == LOGIN_CORRETO and senha == SENHA_CORRETA:
        autenticado = True
        break
    tentativas += 1
    tentativas_restantes = LIMITE_TENTATIVAS - tentativas
    
    if tentativas_restantes > 0:
        print(f"Login ou senha incorretos! Você ainda tem {tentativas_restantes} tentativa(s).\n")

if autenticado:
    print("Acesso permitido! Bem-vindo(a).")
else:
    print("Número máximo de tentativas excedido! Acesso bloqueado.")