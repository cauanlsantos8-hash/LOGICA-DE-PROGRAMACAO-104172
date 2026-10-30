import os

top_5_livros = []

while True:
    os.system("cls")

    print("""=== RANKING TOP 5 LIVROS ===
1 - Adicionar livro ao Top 5
2 - Exibir ranking Top 5
0 - Sair
""")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "1":
            print("\n== CADASTRAR LIVRO ==")
            if len(top_5_livros) >= 5:
                print("Atenção: O Top 5 já está completo! (Limite de 5 livros atingido)")
            else:
                titulo = input(f"Digite o título do {len(top_5_livros) + 1}º livro: ").strip()
                
                if titulo == "":
                    print("O título não pode ficar vazio.")
                elif titulo in top_5_livros:
                    print(f"O livro '{titulo}' já está no ranking!")
                else:
                    top_5_livros.append(titulo)
                    print(f"Livro '{titulo}' adicionado ao Top 5 com sucesso!")

            input("\nPressione Enter para continuar...")

        case "2":
            print("\n== RANKING ATUAL DO TOP 5 ==")
            if not top_5_livros:
                print("Nenhum livro cadastrado no momento.")
            else:
                for posicao, livro in enumerate(top_5_livros, start=1):
                    print(f"{posicao}º Lugar: {livro}")
                print(f"\nTotal cadastrado: {len(top_5_livros)}/5")

            input("\nPressione Enter para continuar...")

        case "0":
            print("\nEncerrando o sistema de Top 5 Livros. Até logo!")
            break

        case _:
            print("\nOpção inválida!")
            input("\nPressione Enter para continuar...")