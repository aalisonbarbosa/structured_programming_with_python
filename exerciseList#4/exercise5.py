# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

def validarDados(dadoA, dadoB):
    try:
        dadoA, dadoB = float(dadoA), float(dadoB)
        return True
    except ValueError:
        print("Informe números válidos.")
        return False

loopingInfinito = False

while True:
    populacaoA = input("Informe o número de habitantes da população A: ")
    populacaoB = input("Informe o número de habitantes da população B: ")

    if validarDados(dadoA=populacaoA, dadoB=populacaoB):
        populacaoA, populacaoB = float(populacaoA), float(populacaoB)
        if populacaoA < 1 or populacaoB < 1:
            print("Informe números acima de 0.")
            continue
        if populacaoA > populacaoB:
            print("O número de habitantes da população A não pode ser maior que o da população B.")
            continue

    taxaCrescimentoPopulacaoA = input("Informe a taxa(%) de crescimento da população A: ")
    taxaCrescimentoPopulacaoB = input("Informe a taxa(%) de crescimento da população B: ")

    if validarDados(dadoA=taxaCrescimentoPopulacaoA, dadoB=taxaCrescimentoPopulacaoB):
        taxaCrescimentoPopulacaoA, taxaCrescimentoPopulacaoB = (float(taxaCrescimentoPopulacaoA)/100)+1, (float(taxaCrescimentoPopulacaoB)/100)+1

    anosNecessarios = 0

    if taxaCrescimentoPopulacaoA <= taxaCrescimentoPopulacaoB:
        if populacaoA < populacaoB:
            print("A população A nunca será maior que a população B com as taxas de crescimento atuais.")
            loopingInfinito = True
            break

    while populacaoA < populacaoB:

        anosNecessarios =  anosNecessarios + 1

        populacaoA = populacaoA * taxaCrescimentoPopulacaoA
        populacaoB = populacaoB * taxaCrescimentoPopulacaoB

        print(populacaoA,populacaoB)
    break

if not loopingInfinito:
    print("O número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B:")
    print(f"{anosNecessarios} anos.")