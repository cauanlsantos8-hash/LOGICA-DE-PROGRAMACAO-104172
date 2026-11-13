import os
os.system('cls')

# Função com parâmentro e com retorno.
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

print('= Solicitando Notas =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parâmentro e
# inserindo o retorno na variável soma.
soma = calcular_notas(nota1, nota2)

print('= Exibindo Notas =')
print(f'Soma: {soma}')