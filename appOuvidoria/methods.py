def listarReclamacoes(listaReclamacoes):
    if len(listaReclamacoes) < 1:
        print(f"\n❌ Não há reclamções cadastradas.\n")
    else:
        print(f"\nLista de reclamações:")
        for num in range(len(listaReclamacoes)):
            print(f"Reclamção {num+1}) {listaReclamacoes[num]}")
        print()

def criarReclamacao(listaReclamacoes, novaReclamacao):
    if len(novaReclamacao) == 0:
        return False
    else:
        listaReclamacoes.append(novaReclamacao)
        return True

def exibirQuantidadeTotalReclamacoes(listaReclamacoes):
    if len(listaReclamacoes) < 1:
        print(f"\n❌ Não há reclamações cadastradas.\n")
    else:
        print(f"\n📊 Total de reclamações cadastradas: {len(listaReclamacoes)}\n")

def pesquisarReclamacao(listaReclamacao, codigo):
    if codigo > 0 and codigo <= len(listaReclamacao):
        print(f"\n🔎 Reclamação {codigo}: {listaReclamacao[codigo-1]}\n")
    else:
        print(f"\n❌ Reclamação não encontrada.\n")

def validarNumero(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False