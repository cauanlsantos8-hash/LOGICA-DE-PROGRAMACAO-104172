import os
os.system('cls')

# ENTRADA.
quantidade = int(input('Digite a quantidade de maçãs desejadas: '))

if quantidade <= 0:
    print('Quantidade inválida! Por favor digite um número maior que zero.')
elif quantidade < 12:
    preco_unitario = 1.30
    valor_total = quantidade * preco_unitario
    print(f'O valor total da compra (R$ 1.30/unidade) é: R$ {valor_total:.2}')
else:
    preco_unitario = 1.00
    valor_total = quantidade * preco_unitario
    print(f'O valor total da compra com desconto (R$ 1.00/unidade) é: {valor_total:.2}')


