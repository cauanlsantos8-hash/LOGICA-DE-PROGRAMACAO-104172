import os
os.system('cls')

vetor_nomes = []

for i in range(3):
    nome= input('Lista de nomes: ')
    vetor_nomes.append(nome) # Inserindo a nota no vetor de nomes.

for i in range(3):
    print(f'Nomes: {vetor_nomes[i]}')