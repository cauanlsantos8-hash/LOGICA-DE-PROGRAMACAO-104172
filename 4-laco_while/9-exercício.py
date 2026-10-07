import os
os.system('cls')


soma = 0
contador = 0
resposta = "S"

while resposta.upper() != "N":
    nota = float(input("Digite a nota: "))
    
    soma += nota
    contador += 1
    
    resposta = input("Deseja inserir mais uma nota? (S/N): ")
    print()

if contador > 0:
    media = soma / contador
    print(f"Quantidade de notas inseridas: {contador}")
    print(f"A média aritmética é: {media}")
else:
    print("Nenhuma nota foi inserida.")
