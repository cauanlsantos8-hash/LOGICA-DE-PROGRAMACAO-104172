import os
os.system('cls')

# ENTRADA.
print('= Solicitando notas =')
QUANTIDADE_NOTAS = 3
soma_notas = 0

for i in range(QUANTIDADE_NOTAS):
    soma_notas += float(input('Digite uma nota: '))

# PROCESSAMENTO.
media = soma_notas / QUANTIDADE_NOTAS
print('\n= Exibindo resultados =')
print(f'Média:{media}')

# SAÍDA.
print(f"\nMédia do aluno: {media:.2f}")

if media >= 7:
    print("Resultado: ALUNO APROVADO!")
elif media >= 4:
    print('Resultado: ALUNO EM RECUPERAÇÃO.')
else:
    print("Resultado: ALUNO REPROVADO!")
