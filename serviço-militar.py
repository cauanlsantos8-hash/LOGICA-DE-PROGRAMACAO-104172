import os 
os.system('cls')

# ENTRADA.
idade = int(input('Digite sua idade: '))
sexo = input('Digite o sexo: ').upper() 

# PROCESSAMENTO.
if idade >= 18 and sexo == 'masculino':
    resultado = 'Deve apresentar-se ao serviço militar.'
else:
    resultado = 'Não deve apresentar-se ao serviço militar.'

# SAÍDA.
print(f'Resultado: {resultado}')
