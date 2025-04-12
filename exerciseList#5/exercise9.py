# • 9) Crie um método que receba o valor do salario e indique a quantidade de imposto a ser pago (se ganhar até 2000,12%. Acima de 2000, 25%)

salario = float(input("Informe seu salário: "))

def calcImposto(salario):
    if salario <= 2000: 
        taxaImposto = 0.12
    elif salario > 2000:
        taxaImposto = 0.25
    
    imposto = salario * taxaImposto

    return imposto

print(calcImposto(salario))