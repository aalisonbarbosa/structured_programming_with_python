from operacoesbd import *
from methods import *

conn = criarConexao("127.0.0.1","root","12345","appLocadora2")

opcao = -1

while opcao:
    print("1) Listar \n2) Adicionar \n3) Pesquisar \n4) Remover \n5) Substituir \n6) Quantidade \n7) Sair")
    opcao = int(input("Digite a sua opção: "))
    
    if opcao == 1:

        listaFilmes = listarFilmes(conn)

        if len(listaFilmes) == 0:
            print("Não há filmes cadastrados!")
        else:
            for filme in listaFilmes:
                print(f"- filme: código: {filme[0]} {filme[1]}, lançado no ano {filme[3]}.")

    elif opcao == 2:

        nome = input("Digite o nome do novo filme: ")
        sinopse = input("Digite a sinopse do novo filme: ")
        ano = int(input("Digite o ano do novo filme: "))

        adicionarFilme(conn, nome, ano, sinopse)

        print("Filme inserido com sucesso!")

    elif opcao == 3:   

        codigo = int(input("Digite o código para pesquisa: "))

        filme = pesquisarFilmeCodigo(conn, codigo)

        if len(filme) == 0:
            print("Não existem filmes a serem exibidos")
        else:
            print(f"- filme: {filme[0][1]}, lançado no ano {filme[0][3]}.")

    elif opcao == 4:

        codigo = int(input("Digite o código para remover: "))

        linhasAfetadas = removerFilmeCodigo(conn, codigo)

        if linhasAfetadas == 0:
            print("Nenhum filme removido")
        else:
            print("Filme removido com sucesso!")

    elif opcao == 5:

        novoNome = input("Digite o novo nome do filme: ")
        codigo = int(input("Digite o código para mudar o nome do filme: "))
    
        linhasAfetadas = atualizarNomeFilme(conn, novoNome, codigo)

        if linhasAfetadas == 0:
            print("Nenhum filme atualizado.")
        else:
            print("Filme alterado com sucesso!")

    elif opcao == 6:
        
        quantidadeFilmes = obterQuantidadeFilmes(conn)

        if quantidadeFilmes == 0:
            print("Não há filmes cadastrados!")
        else:
            print(f"Atualmente temos {quantidadeFilmes} filmes cadastrados!")

    elif opcao != 7:
        print("Opção inválida!")
    else:
        break

encerrarConexao(conn)