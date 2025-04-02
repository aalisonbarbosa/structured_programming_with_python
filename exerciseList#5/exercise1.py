# 1) Crie um método que receba um valor em reais e converta a dólares

valorDolares = float(input("Informe um valor em dólares: "))

def converterDolares(x):
    dolares = x / 5.73

    return dolares

print(converterDolares(valorDolares))
