from operacoesbd import *

def listarFilmes(conn):
    consultaListagem = "select * from filmes"
    filmes = listarBancoDados(conn, consultaListagem)

    if len(filmes) == 0:
        print("Não há filmes cadastrados!")
    else:
        for filme in filmes:
            print(f"- filme: código: {filme[0]} {filme[1]}, lançado no ano {filme[3]}.")

def adicionarFilme(conn):
    nome = input("Digite o nome do novo filme: ")
    sinopse = input("Digite a sinopse do novo filme: ")
    ano = int(input("Digite o ano do novo filme: "))

    sql = "insert into filmes(nome, sinopse, ano)values(%s,%s,%s)"

    dados =  [nome, sinopse, ano]

    insertNoBancoDados(conn, sql, dados)
    print("Filme inserido com sucesso!")

def pesquisarPeloCodigo(conn):
    codigo = int(input("Digite o código para pesquisa: "))
    sql = "select * from filmes where id = %s"
    dados = [codigo]

    filmes = listarBancoDados(conn, sql, dados)

    if len(filmes) == 0:
        print("Não existem filmes a serem exibidos")
    else:
        print(f"- filme: {filmes[0][1]}, lançado no ano {filmes[0][3]}.")

def removerFilmePeloCodigo(conn):
    codigo = int(input("Digite o código para remover: "))
    sql = "delete from filmes where id = %s"
    dados = [codigo]

    linhasAfetadas = excluirBancoDados(conn,sql, dados)

    if linhasAfetadas == 0:
        print("Nenhum filme removido")
    else:
        print("Filme removido com sucesso!")

def atualizarNomeFilme(conn):
    codigo = int(input("Digite o código para mudar o nome do filme: "))
    novoNome = input("Digite o novo nome do filme: ")
    sql = "update filmes set nome = %s where id = %s"
    dados = [novoNome, codigo]

    linhasAfetadas = atualizarBancoDados(conn,sql, dados)

    if linhasAfetadas == 0:
        print("Nenhum filme atualizado.")
    else:
        print("Filme alterado com sucesso!")

def obterQuantidadeFilmes(conn):
    sql = "select count(*) from filmes"
    
    resultado = listarBancoDados(conn, sql)
    quantidadeFilmes = resultado[0][0]

    if quantidadeFilmes == 0:
        print("Não há filmes cadastrados!")
    else:
        print(f"Atualmente temos {quantidadeFilmes} filmes cadastrados!")