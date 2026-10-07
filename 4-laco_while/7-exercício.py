import os
os.system('cls')


nota1 = float(input("Digite a primeira nota (0 a 10): "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota inválida. Digite a primeira nota novamente (0 a 10): "))

nota2 = float(input("Digite a segunda nota (0 a 10): "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota inválida. Digite a segunda nota novamente (0 a 10): "))

nota3 = float(input("Digite a terceira nota (0 a 10): "))
while nota3 < 0 or nota3 > 10:
    nota3 = float(input("Nota inválida. Digite a terceira nota novamente (0 a 10): "))

media = (nota1 + nota2 + nota3) / 3

print(f"\nMédia do aluno: {media:}")

if media >= 7.0:
    print("Situação: APROVADO")
elif media >= 5.0:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")