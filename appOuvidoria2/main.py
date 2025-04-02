from operacoesbd import * 
from methods import *

conn = criarConexao("localhost","root","12345","app_ouvidoria")

opcao = -1

while opcao != 7:
    print("======================")
    print("        OPÇÕES        ")
    print("======================")
    print("1) Listagem das Manifestações.\n2) Listagem de Manifestações por Tipo.\n3) Criar uma nova Manifestação.\n4) Exibir quantidade de manifestações.\n5) Pesquisar uma manifestação por código.\n6) Excluir uma Manifestação pelo Código.\n7) Sair do Sistema.\n")

    opcao = input("Digite sua opção: ")

    if validarNumero(opcao):
       opcao = int(opcao)
    else: 
        print("⚠️  Digite uma opção válida!")

    if opcao == 1:

        listarManifestacoes(conn)

    elif opcao == 2:

        categoria = escolherCategoria()
        
        if len(categoria) > 0:
            listarManifestacoesCategoria(conn, categoria)

    elif opcao == 3:

        categoria = escolherCategoria()
        assunto = input("Digite sua manifestação: ")

        criarManifestacao(conn,categoria, assunto)
        
        print(f"✅ Nova manifestação criada com sucesso!")

    elif opcao == 4:

        exibirQuantidadeManifestacoes(conn)

    elif opcao == 5:
        
        codigo = input("Digite o código da manifestação que deseja pesquisar: ")

        if validarNumero(codigo):
          codigo = int(codigo)
        else: 
            print("⚠️  Digite um código válido!")

        pesquisarManifestacaoCodigo(conn, codigo)

    elif opcao == 6:

        codigo = input("Digite o código da manifestação que deseja excluir: ")

        if validarNumero(codigo):
          codigo = int(codigo)
        else: 
            print("⚠️  Digite um código válido!")

        linhasAfetadas = excluirManifestacao(conn, codigo)

        if linhasAfetadas == 0:
            print("❌ Nenhuma manifestação excluída!")
        else:
            print("✅ Manifestação excluída com sucesso!")

    elif opcao != 7:
        print("⚠️  Digite uma opção válida!")

encerrarConexao(conn)