import os
os.system('cls')

# ENTRADA.
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
# PROCESSAMENTO.
imc = peso / (altura * altura)
print('\nSeu IMC é: {imc: .1f}')

# SAÍDA.
if imc < 18.5:
    resultado = 'Abaixo do peso'
elif imc <= 24.9:
    resultado =  'peso ideal (parabéns)'
elif imc <= 29.9:
    resultado = 'levemente acima do peso'
elif imc <= 34.9:
    resultado = 'obesidade grau I'
elif imc <= 39.9:
    resultado = 'obesidade grau II (severa)'
else: # acima de 40
    print('Classificação: obesidade III (mórbida)')
