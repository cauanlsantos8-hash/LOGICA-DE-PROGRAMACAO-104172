import os
os.system('cls')

# ENTRADA.
print('= Solicitando notas =')
QUANTIDADE_NOTAS = 4
soma_notas = 0

for i in range(QUANTIDADE_NOTAS):
    soma_notas += float(input('Digite uma nota: '))

# PROCESSAMENTO.
media = soma_notas / QUANTIDADE_NOTAS

# SAÍDA.
print('\n= Exibindo resultados =')
print(f'Média:{media}')