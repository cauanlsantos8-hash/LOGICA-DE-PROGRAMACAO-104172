import os
os.system('cls')


dia = int(input("Digite um número referente ao dia da semana (1 a 7): "))

match dia:
    case 1 | 7:
        print("Final de semana.")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil.")
    case _:
        print("Dia inválido.")