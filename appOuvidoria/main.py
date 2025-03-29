from methods import *

listaReclamacoes = []
listaSugestoes = []
listaElogios = []

opcoes = {
    1: ("reclamação", "reclamações", listaReclamacoes),
    2: ("sugestão", "sugestões", listaSugestoes),
    3: ("elogio", "elogios", listaElogios)
}

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