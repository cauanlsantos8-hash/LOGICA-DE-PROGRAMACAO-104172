import os

# Limpa o terminal.
os.system('cls')

# ENTRADA.
print('= SOLICITANDO DADOS =')
salario_informado = float(input('Digite o valor do seu salário: '))

# PROCESSAMENTO.
salario_minimo = 1621
quantidade_salarios = salario_informado / salario_minimo

# SAÍDA.
print('= SOLICITANDO DADOS =')
print('Quantidade de salários: ', quantidade_salarios)
print(f'Quantidade de salários: {quantidade_salarios:.3f}')