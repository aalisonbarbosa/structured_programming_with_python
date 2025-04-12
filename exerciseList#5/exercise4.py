# • 4) Crie um método que receba o peso e altura e retorne o IMC.

peso = float(input("Informe seu peso: "))
alt = float(input("Informe sua altura (m): "))

def calcIMC(peso, alt):
    imc = peso / alt**2

    return imc

print(calcIMC(peso, alt))