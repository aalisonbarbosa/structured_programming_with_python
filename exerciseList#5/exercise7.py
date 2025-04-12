# • 7) Crie um método que receba o valor em celsius e converta a farenheit

temperatura = float(input("Informe uma temperatura: "))

def converterTemp(temp):
    tempFah = (temp*1.8) + 32

    return tempFah

print(converterTemp(temperatura))