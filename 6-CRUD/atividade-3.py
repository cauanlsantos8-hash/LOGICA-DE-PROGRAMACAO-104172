import os
import time

def obter_texto_valido(mensagem):
    """Garante que nome ou posição não fiquem em branco."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("-> Erro: O campo não pode ficar em branco. Tente novamente.")


def obter_camisa_valida(mensagem, jogadores, idx_ignorar=None):
    """Valida se a camisa é um inteiro positivo e se não está duplicada no elenco."""
    while True:
        try:
            camisa = int(input(mensagem).strip())
            if camisa <= 0:
                print("-> Erro: O número da camisa deve ser um número inteiro positivo (> 0).")
                continue

            camisa_duplicada = False
            for index, jogador in enumerate(jogadores):
                if idx_ignorar is not None and index == idx_ignorar:
                    continue
                if jogador["camisa"] == camisa:
                    camisa_duplicada = True
                    break

            if camisa_duplicada:
                print(f"-> Erro: A camisa #{camisa} já está cadastrada para outro jogador!")
                continue

            return camisa
        except ValueError:
            print("-> Erro: Digite apenas números inteiros válidos para a camisa.")


def cadastrar_jogador(jogadores):
    """Cadastra um novo jogador solicitando Nome, Posição e Camisa."""
    print("\n== CADASTRAR JOGADOR ==")
    nome = obter_texto_valido("Nome: ")
    posicao = obter_texto_valido("Posição: ")
    camisa = obter_camisa_valida("Camisa: ", jogadores)
    time.sleep(2)


    jogadores.append({"nome": nome, "posicao": posicao, "camisa": camisa})
    print("Jogador cadastrado!")


def listar_jogadores(jogadores):
    """Exibe todos os jogadores no formato solicitado: '1. Lucas Lima | Goleiro | #1'."""
    print("\n== LISTA DE JOGADORES ==")
    if not jogadores:
        print("O elenco está vazio.")
        return False

    for idx, jogador in enumerate(jogadores, start=1):
        print(f"{idx}. {jogador['nome']} | {jogador['posicao']} | #{jogador['camisa']}")
    return True


def selecionar_indice_valido(jogadores, acao):
    """Exibe a lista e valida se a opção informada pertence a um jogador existente."""
    if not listar_jogadores(jogadores):
        return None

    try:
        numero = int(input(f"\nDigite o número do jogador para {acao}: "))
        if 1 <= numero <= len(jogadores):
            return numero - 1
        else:
            print("-> Erro: Número de jogador inexistente na listagem.")
    except ValueError:
        print("-> Erro: Entrada inválida! Digite apenas o número do jogador.")

    return None


def atualizar_jogador(jogadores):
    """Atualiza Nome, Posição e Camisa de um jogador selecionado pelo índice."""
    print("\n== ATUALIZAR JOGADOR ==")
    idx = selecionar_indice_valido(jogadores, "atualizar")
    if idx is not None:
        print("\nDigite os novos dados abaixo: ")
        novo_nome = obter_texto_valido("Novo Nome: ")
        nova_posicao = obter_texto_valido("Nova Posição: ")
        nova_camisa = obter_camisa_valida("Nova Camisa: ", jogadores, idx_ignorar=idx)

        jogadores[idx]["nome"] = novo_nome
        jogadores[idx]["posicao"] = nova_posicao
        jogadores[idx]["camisa"] = nova_camisa
        print("Jogador atualizado com sucesso!")


def excluir_jogador(jogadores):
    """Remove o jogador selecionado da lista."""
    print("\n== EXCLUIR JOGADOR ==")
    idx = selecionar_indice_valido(jogadores, "excluir")
    if idx is not None:
        removido = jogadores.pop(idx)
        print(f"Jogador {removido['nome']} (#{removido['camisa']}) removido do elenco com sucesso!")
        time.sleep(2)



def buscar_jogador(jogadores):
    """Busca por nome, posição ou número da camisa."""
    print("\n== BUSCAR JOGADOR ==")
    if not jogadores:
        print("O elenco está vazio.")
        return

    termo = obter_texto_valido("Digite o nome, posição ou número da camisa para buscar: ").lower()
    encontrados = []

    for idx, jogador in enumerate(jogadores, start=1):
        if (
            termo in jogador["nome"].lower()
            or termo in jogador["posicao"].lower()
            or termo == str(jogador["camisa"])
        ):
            encontrados.append((idx, jogador))

    if encontrados:
        print(f"\nJogadores encontrados ({len(encontrados)}):")
        for idx, jogador in encontrados:
            print(f"{idx}. {jogador['nome']} | {jogador['posicao']} | #{jogador['camisa']}")
    else:
        print("Nenhum jogador encontrado com o termo informado.")


def main():
    jogadores = []

    while True:
        os.system("cls")
        print("""
== GERENCIAMENTO DE ELENCO ==
1. Cadastrar jogador
2. Listar jogadores
3. Atualizar jogador
4. Excluir jogador
5. Buscar jogador
0. Sair
""")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            cadastrar_jogador(jogadores)
        elif opcao == "2":
            listar_jogadores(jogadores)
        elif opcao == "3":
            atualizar_jogador(jogadores)
        elif opcao == "4":
            excluir_jogador(jogadores)
        elif opcao == "5":
            buscar_jogador(jogadores)
        elif opcao == "0":
            print("\nSaindo do programa... Até logo!")
            break
        else:
            print("-> Opção inválida! Escolha uma opção entre 0 e 5.")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()