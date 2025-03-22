listaReclamacoes = []
listaSugestoes = []
listaElogios = []

opcoes = {
    1: ("reclamação", "reclamações", listaReclamacoes),
    2: ("sugestão", "sugestões", listaSugestoes),
    3: ("elogio", "elogios", listaElogios)
}

def listar(lista, manifestacao, manifestacaoPlural):
    if len(lista) < 1:
        print(f"\n❌ Não há {manifestacaoPlural} cadastradas.\n")
    else:
        print(f"\nLista de {manifestacaoPlural}:")
        for num in range(len(lista)):
            print(f"{manifestacao.capitalize()} {num+1}) {lista[num]}")

def criar(lista, manifestacao):
    novaManifestacao = input(f"\nDescreva sua nova {manifestacao}: ")

    if len(novaManifestacao) < 1:
        print(f"\n⚠️ Informe uma {manifestacao} válida!\n")
    else:
        lista.append(novaManifestacao)
        print(f"\n✅ {manifestacao.capitalize()} cadastrada com sucesso! O seu código é {len(lista)}\n")

def exibir(lista, manifestacao):
    if len(lista) < 1:
        print(f"\n❌ Não há {manifestacao} cadastradas.\n")
    else:
        print(f"\n📊 Total de {manifestacao} cadastradas: {len(lista)}\n")

def pesquisar(lista, manifestacao):
    codigoManifestacao = input(f"\nInforme o código do {manifestacao}: ")

    if not validarNumero(codigoManifestacao):
        return
    
    codigoManifestacao = int(codigoManifestacao)

    if codigoManifestacao > 0 and codigoManifestacao <= len(lista):
        print(f"\n🔎 {manifestacao.capitalize()} {codigoManifestacao}: {lista[codigoManifestacao-1]}\n")
    else:
        print(f"\n❌ {manifestacao.capitalize()} não encontrada.\n")

def validarNumero(num):
    try:
        num = int(num)
        return True
    except ValueError:
        print("\n⚠️ Informe um código válido!\n")
        return False

def menu(manifestacao, manifestacaoPlural):
    print("\n============================")
    print(f"         {manifestacaoPlural.upper()}          ")
    print("============================\n")
    print(f"1) Listar os {manifestacaoPlural}.")
    print(f"2) Criar um novo {manifestacao}.")
    print(f"3) Exibir quantidade de {manifestacaoPlural}.")
    print(f"4) Pesquisar um {manifestacao} por código.")
    print(f"5) Sair do serviço.\n")

def servicos(lista, manifestacao, manifestacaoPlural):
    while True:
        menu(manifestacao, manifestacaoPlural)

        opcao = input("Informe sua opção: ")

        if validarNumero(opcao):  
            opcao = int(opcao)

        if opcao == 1:
            listar(lista, manifestacao, manifestacaoPlural)
        elif opcao == 2:
            criar(lista, manifestacao)
        elif opcao == 3:
            exibir(lista, manifestacao)
        elif opcao == 4:
            pesquisar(lista, manifestacao)
        elif opcao == 5:
            break
        else:
            print("\n⚠️ Opção inválida. Tente novamente!\n")

while True:

    print("\n============================")
    print("  LISTA DE MANIFESTAÇÕES  ")
    print("============================\n")
    print("1) Enviar uma reclamação")
    print("2) Enviar uma sugestão")
    print("3) Enviar um elogio")
    print("4) Sair do sistema\n")

    servico = input("Escolha um serviço: ")

    if not servico.isdigit():
        print("\n⚠️ Serviço inválido. Tente novamente!\n")
        continue

    servico = int(servico)

    if servico in opcoes:
        manifestacao, manifestacaoPlural, lista = opcoes[servico]
        servicos(lista, manifestacao, manifestacaoPlural)
    elif servico == 4:
        print("\n✅ Obrigado pelo seu feedback! Saindo do sistema...\n")
        break
    else:
        print("\n⚠️ Opção inválida. Tente novamente!\n")