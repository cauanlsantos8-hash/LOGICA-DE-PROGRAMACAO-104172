import os
os.system('cls')

# ENTRADA.
quantidade = int(input('Digite a quantidade desejada: '))

# PROCESSAMENTO.
if quantidade < 12:
    preco = 1.30
else:
    preco = 1.0

valor_total = quantidade * preco

# SAÍDA.
print(f'Valor total: {valor_total}')