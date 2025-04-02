from operacoesbd import *

def escolherCategoria():
        print("======================")
        print("      CATEGORIAS      ")
        print("======================")
        print("1) Reclamação\n2) Sugestão\n3) Elogios")

        escolha = input("Escolha a categoria da manifestação: ")
        
        if validarNumero(escolha):
            escolha = int(escolha)
        else: 
            print("⚠️  Digite uma opção válida!")

        if escolha > 0 and escolha < 4:
            if escolha == 1:
                categoria = "reclamação"
            elif escolha == 2:
                categoria = "sugestão"
            elif escolha == 3:
                categoria = "elogio"

            return categoria
        else:
            print("⚠️  Digite uma opção válida!")
            return ""

def validarNumero(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False

def listarManifestacoes(conn):
    sql = "select * from manifestacoes"

    manifestacoes = listarBancoDados(conn, sql)

    if len(manifestacoes) == 0:
        print("❌ Não há manifestações cadastradas!")
    else:
        print("Lista de manifestações:")
        for manifestacao in manifestacoes:
            print(f"manifestação {manifestacao[0]}) categoria: {manifestacao[1]} - {manifestacao[2]}")

def listarManifestacoesCategoria(conn, categoria):
    sql = "select * from manifestacoes where categoria = %s"
    dados = [categoria]

    manifestacoes =  listarBancoDados(conn, sql, dados)

    if len(manifestacoes) == 0:
        print("❌ Não há manifestações cadastradas!")
    else:
        print("Lista de manifestações:")
        for manifestacao in manifestacoes:
            print(f"manifestação {manifestacao[0]}) categoria: {manifestacao[1]} - {manifestacao[2]}")

def criarManifestacao(conn, categoria, assunto):
    
    sql = "insert into manifestacoes(categoria, assunto)values(%s,%s)"
    dados = [categoria, assunto]

    insertNoBancoDados(conn, sql, dados)


def exibirQuantidadeManifestacoes(conn):
    sql = "select count(*) from manifestacoes"

    quantidadeManifestacoes = listarBancoDados(conn, sql)

    print(f"No momento temos {quantidadeManifestacoes[0][0]} manifestações cadastradas!")

def pesquisarManifestacaoCodigo(conn, codigo):
    sql = "select * from manifestacoes where id = %s"
    dados = [codigo]

    manifestacao = listarBancoDados(conn, sql, dados)

    if len(manifestacao) == 0:
        print("❌ Manifestação não encontrada!")
    else:
        print(f"🔎 manifestação {manifestacao[0][0]}) categoria: {manifestacao[0][1]} - {manifestacao[0][2]}")

def excluirManifestacao(conn, codigo):
    sql = "delete from manifestacoes where id = %s"
    dados = [codigo]

    linhasAfetadas = excluirBancoDados(conn, sql, dados)

    return linhasAfetadas