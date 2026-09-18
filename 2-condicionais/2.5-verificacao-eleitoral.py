import os
os.system('cls')

idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Não podem votar.')
elif idade <= 17:
    print('Voto opcional.')
elif idade <= 65: 
    print('Voto obrigatório.')
else:
    print('Não é obrigado a votar.')