import os

# Limpa o terminal.
os.system('cls')

# ENTRADA.
print('= VERIFICAÇÃO ELEITORAL =')
idade = int(input('Digite a idade da pessoa: '))

# PROCESSAMENTO.
if idade < 16:
    print('Resultado: NÃO PODE VOLTAR.')
elif (idade >= 16 and idade <= 17) or (idade > 65):
    print('Resultado: VOTO OPCIONAL.')

# SAÍDA.
elif idade >= 18 and idade <= 65:
    print('Resultado: VOTO OBRIGATÓRIO.')