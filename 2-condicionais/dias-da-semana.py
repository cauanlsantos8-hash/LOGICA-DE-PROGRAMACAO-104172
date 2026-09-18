import os
os.system('cls')

dia = input('Digite o dia da semana: ').lower()

match dia:
    case 'Segunda':
        print('Hoje é Segunda-Feira.')
    case 'Terça':
        print('Hoje é Terça-Feira.')
    case 'Quarta':
        print('Hoje é Quarta-Feira.')
    case 'Quinta':
        print('Hoje é Quinta-Feira.')
    case 'Sexta':
        print('Hoje é Sexta-Feira.')
    case 'Sábado' | 'Domingo':
        print('Hoje é Fim de Semana!')
    case _:
        print('Dia inválido.')

        print(dia)
        
        print('=== FIM ===')