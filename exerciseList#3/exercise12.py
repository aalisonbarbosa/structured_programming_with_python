# Faça um Programa que peça uma data no formato dd/mm/aaaae determine se a mesma é uma data válida.

diasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    print("Digite uma data no formato dd/mm/aaaa:")
    data = input("Data: ")

    if data.count("/") != 2:
        print("Data inválida!")
        continue

    dia, mes, ano = data.split("/")

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if mes < 1 or mes > 12:
        print("Mês inválido!")
        continue
    elif mes == 2:
        # verifica se o ano é bisexto
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia < 1 or dia > 29:
                print("Dia inválido!")
                continue
            else:
                print("Data válida!")
        else:
            if dia < 1 or dia > 28:
                print("Dia inválido!")
                continue
            else:
                print("Data válida!")
    else:
        if dia < 1 or dia > diasMeses[mes - 1]:
            print("Dia inválido!")
            continue
        else:
            print("Data válida!")
    break