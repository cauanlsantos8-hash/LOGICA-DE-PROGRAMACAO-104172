import os
os.system('cls')


# ENTRADA
print('= Solicitando notas =')
soma = 0

for i in range(4):
    nota = float(input('Digite uma nota: '))
    soma = soma + nota

# PROCESSAMENTO.
    media = soma / 4

# SAÍDA.
print('\n= Exibindo resultados =')
print(f'Média: {media}')
