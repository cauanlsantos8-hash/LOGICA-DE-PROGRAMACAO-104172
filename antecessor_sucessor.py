import os

# Limpa o terminal.
os.system('cls')

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1

# Mostra o resultado na tela
print(f"O antecessor de {numero} é {antecessor} e o seu sucessor é {sucessor}.")