import os

# Limpa o terminal.
os.system('cls')

# ENTRADA.
print('=ANÁLISE DE DOIS NÚMEROS INTEIROS=')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

# PROCESSAMENTO.
soma = num1 + num2
media = soma / 2
produto = num1 * num2

#PROCESSAMENTO LÓGICO.
if num1 == num2:
    maior = num1
    menor = num1
elif num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

# SAÍDA.
print('\n= RESULTADOS =')
print(f'Média: {media:.2f}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
