from operacoesbd import *

# === Interface de usuário ===
def escolherCategoria():
    exibirMenuCategorias()
    escolha = obterEscolhaCategoria()
    
    if not validarEscolhaCategoria(escolha):
        print("⚠️  Digite uma opção válida!")
        return ""

    return converterEscolhaParaCategoria(int(escolha))

def exibirMenuCategorias():
    print("======================")
    print("      CATEGORIAS      ")
    print("======================")
    print("1) Reclamação\n2) Sugestão\n3) Elogio")

def obterEscolhaCategoria():
    escolha = input("Escolha a categoria da manifestação: ")
    return escolha

def validarEscolhaCategoria(escolha):
    if not validarNumero(escolha):
        return False
    escolha = int(escolha)
    return 1 <= escolha <= 3

def converterEscolhaParaCategoria(numero):
    categorias = {
        1: "reclamação",
        2: "sugestão",
        3: "elogio"
    }
    return categorias.get(numero, "")

def exibirManifestacoes(manifestacoes):
    if len(manifestacoes) == 0:
        print("❌ Não há manifestações cadastradas!")
    else:
        print("Lista de manifestações:")
        for manifestacao in manifestacoes:
            print(f"manifestação {manifestacao[0]}) categoria: {manifestacao[1]} - {manifestacao[2]}")

# === Operações de banco de dados ===
def buscarManifestacoes(conn):
    sql = "select * from manifestacoes"

    manifestacoes = listarBancoDados(conn, sql)

    return manifestacoes

def buscarManifestacoesCategoria(conn, categoria):
    sql = "select * from manifestacoes where categoria = %s"
    dados = [categoria]

    manifestacoes =  listarBancoDados(conn, sql, dados)

    return manifestacoes

def criarManifestacao(conn, categoria, assunto):
    sql = "insert into manifestacoes(categoria, assunto)values(%s,%s)"
    dados = [categoria, assunto]

    insertNoBancoDados(conn, sql, dados)


def buscarQuantidadeManifestacoes(conn):
    sql = "select count(*) from manifestacoes"

    quantidadeManifestacoes = listarBancoDados(conn, sql)

    return quantidadeManifestacoes

def pesquisarManifestacaoCodigo(conn, codigo):
    sql = "select * from manifestacoes where id = %s"
    dados = [codigo]

    manifestacao = listarBancoDados(conn, sql, dados)

    return manifestacao

def excluirManifestacao(conn, codigo):
    sql = "delete from manifestacoes where id = %s"
    dados = [codigo]

    linhasAfetadas = excluirBancoDados(conn, sql, dados)

    return linhasAfetadas

# === Utilitários ===
def validarNumero(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False