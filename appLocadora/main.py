filmes = []
opcao = -1

while opcao:
    print("Escolha uma opção:\n1)Adicionar\n2)Listar\n3)Sair")
    
    opcao = int(input("Digite sua opção: "))
    
    if opcao == 1:

        novoFilme = input("Digite o nome do filme: ")
        filmes.append(novoFilme)
        print("Filme cadastrado com sucesso!")

    elif opcao == 2:

        if len(filmes) > 0:
            print("Lista de filmes:")
            for item in filmes:
                print("-",item)
        else:
            print("Nenhum filme cadastrado!")

    elif opcao != 3:
        print("Opção inválida!")  
    else:
        break