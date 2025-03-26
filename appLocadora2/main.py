from operacoesbd import *

conn = criarConexao("127.0.0.1","root","12345","appLocadora2")

opcao = -1

while opcao:
    print("Escolha uma opção:\n1)Adicionar\n2)Listar\n3)Sair")
    
    opcao = int(input("Digite sua opção: "))
    
    if opcao == 1:

        nome = input("Digite o nome do novo filme: ")
        sinopse = input("Digite a sinopse do novo filme: ")
        ano = int(input("Digite o ano do novo filme: "))

        sql = "insert into filmes(nome, sinopse, ano)values(%s,%s,%s)"

        dados =  [nome, sinopse, ano]

        insertNoBancoDados(conn, sql, dados)
        print("Filme inserido com sucesso!")

    elif opcao == 2:
        
        consultaListagem = "select * from filmes"
        filmes = listarBancoDados(conn, consultaListagem)

        if len(filmes) == 0:
            print("Não há filmes cadastrados!")
        else:
            for filme in filmes:
                print(f"- filme: {filme[1]}, lançado no ano {filme[3]}.")

    elif opcao != 3:   
        print("Opçaõ inválida!")
    else:
        break

encerrarConexao(conn)