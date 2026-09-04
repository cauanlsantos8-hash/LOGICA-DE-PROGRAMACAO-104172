import os
os.system('cls')

# ENTRADA.
media = float(input("Digite a média do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

# PROCESSAMENTO.
if media >= 7.0 and faltas <= 40:
    print("\nAluno APROVADO!")

# SAÍDA.
else:
    print("\nAluno REPROVADO!")


