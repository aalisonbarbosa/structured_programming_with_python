# • 3) Crie um método que receba 3 parâmetros: um valor, moeda de origem e a moeda que deve ser convertida (dolares, euros ou peso argentino). E realize a conversão.

moedaOrigem = float(input("Informe a moeda de origem:\n1) dólares.\n2) euros.\n3) peso argentino."))
escolha = int(input("Escolha uma moeda que deve ser convertida:\n1) dólares.\n2) euros.\n3) peso argentino."))
valor =  float(input("Informe um valor: ")) 

def converterMoeda(x, moedaOrigem, escolha):
    dolares = 5.73
    euro = 6.2
    pesoArgentino = 0.01

    if escolha == 1:
        moedaConvertida = dolares
    elif escolha == 2:
        moedaConvertida= euro
    else:
        moedaConvertida = pesoArgentino

    if moedaOrigem == 1:
        moedaOrigem = dolares
    elif moedaOrigem == 2:
        moedaOrigem= euro
    else:
        moedaOrigem = pesoArgentino

    conversao =  x * moedaOrigem / moedaConvertida
    
    return conversao

if escolha > 0 and escolha < 4:
    print(converterMoeda(valor, moedaOrigem, escolha))
else: 
    print("Escolha inválida!")