import os

# Limpa o terminal
os.system('cls')

# ENTRADA.
print('= SOLICITANDO DADOS =')
# Usando float para permitir números quebrados (ex: 5.5)
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

# PROCESSAMENTO E SAÍDA.
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero

print('\n= EXIBINDO DADOS =')
print('Soma: ', soma)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)

# Evitando o erro de divisão por zero
if segundo_numero != 0:
    divisao = primeiro_numero / segundo_numero
    print('Divisão: ', divisao)
else:
    print('Divisão: Não é possível dividir por zero!')

