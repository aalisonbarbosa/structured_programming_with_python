def listarManifestacao(lista):
    if len(lista) < 1:
        print(f"\n❌ Não há reclamções cadastradas.\n")
    else:
        print(f"\nLista de reclamações:")
        for num in range(len(lista)):
            print(f"Reclamção {num+1}) {lista[num]}")

def criarManifestacao(lista, novaManifestacao):
    if len(novaManifestacao) < 1:
        return False
    else:
        lista.append(novaManifestacao)
        return True

def exibirQuantidadeTotalManifestacoes(lista):
    if len(lista) < 1:
        print(f"\n❌ Não há reclamações cadastradas.\n")
    else:
        print(f"\n📊 Total de reclamações cadastradas: {len(lista)}\n")

def pesquisarManifestacao(lista, codigoManifestacao):

    if codigoManifestacao > 0 and codigoManifestacao <= len(lista):
        print(f"\n🔎 Reclamação {codigoManifestacao}: {lista[codigoManifestacao-1]}\n")
    else:
        print(f"\n❌ Reclamação não encontrada.\n")

def validarNumero(num):
    try:
        num = int(num)
        return True
    except ValueError:
        return False
