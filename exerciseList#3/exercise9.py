# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutinoou V-Vespertinoou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


while True:
    print("Em qual turno você estuda?")
    turno = input("Digite M para matutino, V para vespertino e N para noturno: ").upper().replace(" ", "")
    if turno == "M":
        print("Bom dia!")
    elif turno == "V":
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Turno inválido!")
        continue
    break