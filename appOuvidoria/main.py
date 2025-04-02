from methods import *

listaReclamacoes = []

while True:

    print("\n============================")
    print("        MANIFESTAÇÕES       ")
    print("============================")
    print("1) Listar as reclamações.")
    print("2) Criar uma nova reclamação.")
    print("3) Exibir quantidade de reclamações.")
    print("4) Pesquisar um reclamação por código.")
    print("5) Sair do programa.\n")

    opcao = input("Informe sua opção: ")

    if validarNumero(opcao):  
        opcao = int(opcao)
    else:
        print("\n⚠️ Informe uma opção válida!\n")
        continue

    if opcao == 1:
            listarManifestacao(listaReclamacoes)
    elif opcao == 2:

        novaManifestacao = input(f"\nDescreva sua nova reclamação: ")
        manifestacao = criarManifestacao(listaReclamacoes, novaManifestacao)

        if manifestacao:
            print(f"\n✅ Reclamação cadastrada com sucesso! O seu código é {len(listaReclamacoes)}\n")
        else: 
            print(f"\n⚠️ Informe uma reclamação válida!\n")

    elif opcao == 3:
        exibirQuantidadeTotalManifestacoes(listaReclamacoes)
    elif opcao == 4:
        
        codigoManifestacao = input(f"\nInforme o código da manifestação: ")

        if validarNumero(codigoManifestacao):
            codigoManifestacao = int(codigoManifestacao)
        else: 
            print("n⚠️ Informe um código válido!")
            continue

        pesquisarManifestacao(listaReclamacoes, codigoManifestacao)

    elif opcao == 5:
        print("\n✅ Obrigado pelo seu feedback! Saindo do sistema...\n")
        break
    else:
        print("\n⚠️ Opção inválida. Tente novamente!\n")