# 1) Crie um método que receba um valor em reais e converta a dólares

'''
def converterDolares(x):
    dolares = x / 5.73
    print(dolares)

converterDolares(300)
'''

# • 2) Crie um método que receba 2 parâmetros: um valor em reais e a moeda que deve ser convertida (dólares, euros ou peso argentino). E realize a conversão.

'''
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
    
    print(conversao)


valor = float(input("Infomer um valor: "))
moedaConvertida = int(input("Escolha uma moeda que deve ser convertida:\n1) dólares.\n2) euros.\n3) peso argentino.")) 

if moedaConvertida > 0 and moedaConvertida < 4:
    converterMoeda(valor, moedaConvertida)
'''

# • 3) Crie um método que receba 3 parâmetros: um valor, moeda de origem e a moeda que deve ser convertida (dolares, euros ou peso argentino). E realize a conversão.

'''
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
    
    print(conversao)

if escolha > 0 and escolha < 4:
    converterMoeda(valor, moedaOrigem, escolha)
'''

# • 4) Crie um método que receba o peso e altura e retorne o IMC.

'''
peso = float(input("Informe seu peso: "))
alt = float(input("Informe sua altura (m): "))

def calcIMC(peso, alt):
    imc = peso / alt**2

    print(imc)

calcIMC(peso, alt)
'''

# • 5) Crie um método que receba as notas e retorne a maior nota do aluno

'''
notas = [8, 7.5, 8.2]

def analisarNotas(nota):

    maiorNota = sorted(nota, reverse=True)[0]

    print(maiorNota)

analisarNotas(notas)
'''

# • 6) Crie um método que receba as notas e retorne a média de notas do aluno

'''
notas = [8, 7.5, 8.2]

def analisarNotas(nota):

    media = sum(nota)/len(nota)

    print(media)

analisarNotas(notas)
'''

# • 7) Crie um método que receba o valor em celsius e converta a farenheit

'''
temperatura = float(input("Informe uma temperatura: "))

def converterTemp(temp):
    tempFah = (temp*1.8) + 32

    print(tempFah)

converterTemp(temperatura)
'''

# • 8) Crie um método que receba o valor em farenheite converta a celsius

'''
temperatura = float(input("Informe uma temperatura: "))

def converterTemp(temp):
    tempCel = ((temp - 32) / 1.8)

    print(tempCel)

converterTemp(temperatura)
'''

# • 9) Crie um método que receba o valor do salario e indique a quantidade de imposto a ser pago (se ganhar até 2000,12%. Acima de 2000, 25%)

'''
salario = float(input("Informe seu salário: "))

def calcImposto(salario):
    if salario <= 2000: 
        imposto = 0.12
    elif salario > 2000:
        imposto = 0.25
    
    calculo = salario * imposto

    print(calculo)

calcImposto(salario)
'''