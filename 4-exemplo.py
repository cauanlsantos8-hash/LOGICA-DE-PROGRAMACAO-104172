import os
os.system('cls')


print('= INSERINDO 5 LIVROS NO VETOR =')
vetor_livros = []




for i in range(5):
    livro = input(f'Digite o nome do {i+1}º Livro: ')
    vetor_livros.append(livro)


print('\n= EXIBINDO OS LIVROS DO VETOR =')
for indice, livro in enumerate(vetor_livros, start=1):
    print(f'{indice}º: {livro}')
