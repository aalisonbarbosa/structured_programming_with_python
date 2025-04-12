from methods import *

listaReclamacoes = []

while True:

    print("============================")
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
            listarReclamacoes(listaReclamacoes)
    elif opcao == 2:

        novaReclamacao = input(f"\nDescreva sua nova reclamação: ")
        reclamacao = criarReclamacao(listaReclamacoes, novaReclamacao)

        if reclamacao:
            print(f"\n✅ Reclamação cadastrada com sucesso! O seu código é {len(listaReclamacoes)}\n")
        else: 
            print(f"\n⚠️ Informe uma reclamação válida!\n")

    elif opcao == 3:
        exibirQuantidadeTotalReclamacoes(listaReclamacoes)
    elif opcao == 4:
        
        codigoReclamacao = input(f"\nInforme o código da manifestação: ")

        if validarNumero(codigoReclamacao):
            codigoReclamacao = int(codigoReclamacao)
        else: 
            print("n⚠️ Informe um código válido!")
            continue

        pesquisarReclamacao(listaReclamacoes, codigoReclamacao)

    elif opcao == 5:
        print("\n✅ Obrigado pelo seu feedback! Saindo do sistema...\n")
        break
    else:
        print("\n⚠️ Opção inválida. Tente novamente!\n")