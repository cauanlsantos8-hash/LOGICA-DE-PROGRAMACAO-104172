import os
os.system('cls')

notas = []

for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\n= NOTAS INFORMADAS =")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")

print(f"\nMédia do aluno: {media}")