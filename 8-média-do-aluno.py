import os

# Limpa o terminal.
os.system('cls')

# ENTRADA.
print("= CÁLCULO DE MÉDIA =")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# PROCESSAMENTO.
media = (nota1 + nota2 + nota3) / 3

# SAÍDA.
print(f"\nMédia do aluno: {media:.2f}")

if media < 7:
    print("Resultado: ALUNO REPROVADO!")
else:
    print("Resultado: ALUNO APROVADO!")