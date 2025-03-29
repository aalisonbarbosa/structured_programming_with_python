from operacoesbd import *
from methods import *

conn = criarConexao("127.0.0.1","root","12345","appLocadora2")

opcao = -1

while opcao:
    print("\n1) Listar \n2) Adicionar \n3) Pesquisar \n4) Remover \n5) Substituir \n6) Quantidade \n7) Sair")
    opcao = int(input("Digite a sua opção: "))
    
    if opcao == 1:
        listarFilmes(conn)
    elif opcao == 2:
        adicionarFilme(conn)
    elif opcao == 3:   
        pesquisarPeloCodigo(conn)
    elif opcao == 4:
        removerFilmePeloCodigo(conn)
    elif opcao == 5:
        atualizarNomeFilme(conn)
    elif opcao == 6:
        obterQuantidadeFilmes(conn)
    elif opcao != 7:
        print("Opção inválida!")
    else:
        break

encerrarConexao(conn)