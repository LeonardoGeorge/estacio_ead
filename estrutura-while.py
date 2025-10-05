# Enquanto a opção escolhida for diferente de 3:
#    se a opção for 1 → adicionar produto
#    se a opção for 2 → mostrar estoque
#    se for qualquer outra → avisar erro
# Quando a opção for 3 → encerrar o sistema

# Criando uma lista vazia para guardar os produtos
estoque = []

# Começamos com uma opção diferente de 3 (para entrar no while)
opcao = 0

# Enquanto o usuário não digitar 4, o programa continua
while opcao != 4:
    print("\n=== MENU DE ESTOQUE ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Mostrar estoque")
    print("4 - Sair")

    # Lendo a escolha do usuário
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        produto = input("Digite o nome do produto: ")
        estoque.append(produto)
        print(f"✅ Produto '{produto}' adicionado com sucesso!")

    elif opcao == 2:
        if len(estoque) == 0:
            print("❌ Estoque vazio! Não há produtos para remover.")
        else:
            produto = input("Digite o nome do produto a ser removido: ")
            if produto in estoque:
                estoque.remove(produto)
                print(f"✅ Produto '{produto}' removido com sucesso!")
            else:
                print(f"❌ Produto '{produto}' não encontrado no estoque!")

    elif opcao == 3:
        if len(estoque) == 0:
            print("⚠️ O estoque está vazio!")
        else:
            print("\n📦 Produtos no estoque:")
            for item in estoque:
                print("-", item)

    elif opcao == 4:
        print("🚪 Encerrando o sistema... até logo!")

    else:
        print("❌ Opção inválida, tente novamente.")










