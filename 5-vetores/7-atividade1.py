import os
os.system('cls')


print('= INSERINDO NOTAS NO VETOR =')
vetor_notas = []
QUANTIDADE_NOTAS = 3


for i in range(QUANTIDADE_NOTAS):
    Nota = float(input(f'Digite a {i+1}º Nota: '))
    vetor_notas.append(Nota)


# Sum - Somar tudo que está no vetor.
media = sum(vetor_notas) / QUANTIDADE_NOTAS




print('\n= EXIBINDO NOTAS =')
for posicao, Nota in enumerate(vetor_notas, start=1):
    print(f'{posicao}º nota: {Nota}')


print(f'Média: {media}')
