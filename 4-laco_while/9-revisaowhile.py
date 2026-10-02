import os
os.system('cls')

nota1 = float(input("Digite a primeira nota (0 a 10): "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota inválida. Digite a primeira nota novamente: "))

nota2 = float(input("Digite a segunda nota (0 a 10): "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota inválida. Digite a segunda nota novamente: "))


media = (nota1 + nota2) / 2


print(f"\nA média aritmética do aluno é: {media:.2f}")