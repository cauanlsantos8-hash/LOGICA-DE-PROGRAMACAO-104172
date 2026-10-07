import os
os.system('cls')

while True:
    print('= MENU DE OPÇÕES =')
    print('1 - X-Tudo ------- R$ 25,90')
    print('2 - X-Salada ----- R$ 15,90')
    print('3 - Cachorro-Quente - R$ 10,90')
    print('4 - Sanduíche ---- R$ 8,90')
    print('5 - Esfirra de Frango - R$ 12,90')


    opção = int(input('\nEscolha uma opção (1 a 5): '))

    if opção == 1:
        print(f'\nOpção escolhida: 1 - X-Tudo')
        print('Preço: R$ 25,90')
        break
    elif opção == 2:
        print('\nOpção escolhida: 2 - X-Salada')
        print('Preço: R$ 15,90')
        break
    elif opção == 3:
        print('\nOpção escolhida: 3 - Cachorro-Quente')
        print('Preço: R$ 10,90')
        break
    elif opção == 4:
        print('\nOpção escolhida: 4 - Sanduíche')
        print('Preço: R$ 8,90')
        break
    elif opção == 5:
        print('\nOpção escolhida: 5 - Esfirra de Frango')
        print('Preço: R$ 12,90')
        break
    else:
        print('\nOpção inválida! Tente Novamente.')