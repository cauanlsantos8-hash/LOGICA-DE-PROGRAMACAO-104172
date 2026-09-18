import os
os.system('cls')

# ENTRADA.
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))
sexo = input("Digite o sexo (M para Masculino ou F para Feminino): ").strip().upper()

# PROCESSAMENTO.
match sexo:
    case 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f"\nSexo: Masculino")
        print(f"Altura: {altura:.2f} m")
        print(f"Peso Ideal: {peso_ideal:.2f} kg")
        
    case 'F':
        peso_ideal = (62.1 * altura) - 44.7
        print(f"\nSexo: Feminino")
        print(f"Altura: {altura:.2f} m")
        print(f"Peso Ideal: {peso_ideal:.2f} kg")
# SAÍDA.
    case _:
        print("\nOpção de sexo inválida! Informe apenas 'M' ou 'F'.")