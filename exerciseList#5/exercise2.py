# • 2) Crie um método que receba 2 parâmetros: um valor em reais e a moeda que deve ser convertida (dólares, euros ou peso argentino). E realize a conversão.

valor = float(input("Infomer um valor: "))
moedaConvertida = int(input("Escolha uma moeda que deve ser convertida:\n1) dólares.\n2) euros.\n3) peso argentino.")) 

def converterMoeda(x, moeda):
    dolares = 5.73
    euro = 6.2
    pesoArgentino = 0.01

    if moeda == 1:
        conversao = x / dolares
    elif moeda == 2:
        conversao = x / euro
    else:
        conversao = x / pesoArgentino
    
    return conversao

if moedaConvertida > 0 and moedaConvertida < 4:
    print(converterMoeda(valor, moedaConvertida))
