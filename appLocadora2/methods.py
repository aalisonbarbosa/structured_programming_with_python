from operacoesbd import *

def listarFilmes(conn):
    sql = "select * from filmes"
    filmes = listarBancoDados(conn, sql)

    return filmes

def adicionarFilme(conn, nome, sinopse, ano):
    sql = "insert into filmes(nome, sinopse, ano)values(%s,%s,%s)"
    dados =  [nome, sinopse, ano]

    insertNoBancoDados(conn, sql, dados)

def pesquisarFilmeCodigo(conn, codigo):
    sql = "select * from filmes where id = %s"
    dados = [codigo]

    filmes = listarBancoDados(conn, sql, dados)

    return filmes

def removerFilmeCodigo(conn, codigo):
    sql = "delete from filmes where id = %s"
    dados = [codigo]

    linhasAfetadas = excluirBancoDados(conn,sql, dados)

    return linhasAfetadas

def atualizarNomeFilme(conn, novoNome, codigo):
    
    sql = "update filmes set nome = %s where id = %s"
    dados = [novoNome, codigo]

    linhasAfetadas = atualizarBancoDados(conn,sql, dados)

    return linhasAfetadas

def obterQuantidadeFilmes(conn):
    sql = "select count(*) from filmes"   
    
    resultado = listarBancoDados(conn, sql)
    quantidadeFilmes = resultado[0][0]

    return quantidadeFilmes