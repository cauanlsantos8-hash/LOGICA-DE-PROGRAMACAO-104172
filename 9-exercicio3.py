import os
os.system('cls')


notas = []

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\n= NOTAS INFORMADAS =")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")

print(f"\nMédia do aluno: {media}")

if media >= 7.0:
    print("Situação: APROVADO")
elif media >= 5.0:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")