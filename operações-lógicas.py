import os
os.system('cls')

# ENTRADA.
matricula = input("Digite o código/matrícula do empregado: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
tempo_trabalho = int(input("Digite o tempo de trabalho (em anos): "))

# PROCESSAMENTO.
ano_atual = 2026
idade = ano_atual - ano_nascimento

if idade >= 65 or tempo_trabalho >= 30:
    mensagem = "Requerer aposentadoria"
else:
    mensagem = "Não requerer aposentadoria"

# SAÍDA.
print("\n= RESULTADO DA ANÁLISE =")
print(f"Código do empregado: {matricula}")
print(f"Idade: {idade} anos")
print(f"Tempo de trabalho: {tempo_trabalho} anos")
print(f"Situação: {mensagem}")