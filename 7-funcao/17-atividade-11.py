import os
os.system('cls')

def calcular_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)

def mostrar_resultado(media, lista_notas):
    print('\n= EXIBINDO NOTAS =')
    for nota in lista_notas:
        print(f'Nota: {nota}')

    print(f'\nMedia: {media}')

lista_notas = []

for i in range(3):
    nota = float(input('Digite uma nota: '))
    lista_notas. append (nota)

media = calcular_notas(lista_notas)

mostrar_resultado(media, lista_notas)