import os

# Limpa o terminal.
os.system('cls')

# ENTRADA.
print('= SOLICITANDO DADOS =')
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

# PROCESSAMENTO.
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

# SAÍDA.
print('\n= EXIBINDO DADOS =')
print('Soma: ', soma)
print('Subtração: ', subtracao)
print('multiplicação: ', multiplicacao)
print('Divisão: ', divisao)