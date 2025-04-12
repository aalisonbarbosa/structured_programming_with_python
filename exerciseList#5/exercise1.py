# 1) Crie um método que receba um valor em reais e converta a dólares

valorReais = float(input("Informe um valor em reais: "))

def converterDolares(x):
    dolares = x / 5.73

    return dolares

print(converterDolares(valorReais))