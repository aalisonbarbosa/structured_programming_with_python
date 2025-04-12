#11 As Organizações Hamurabi Medeiros resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# • Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 
# • salários até R$ 280,00 (incluindo) : aumento de 20% 
# • salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
# • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% 
# • salários de R$ 1500,00 em diante : aumento de 5% 
# • Após o aumento ser realizado, informe na tela: 
# • o salário antes do reajuste; 
# • o percentual de aumento aplicado; 
# • o valor do aumento; 
# • o novo salário, após o aumento.

salarioAtual = float(input("Salário atual: "))

if salarioAtual > 0:
    if salarioAtual <= 280:

        aumento = salarioAtual * 0.2
        percentualAumento = "20%"
        salarioReajustado = salarioAtual + aumento

    if salarioAtual > 280 and salarioAtual <= 700:

        aumento = salarioAtual * 0.15
        percentualAumento = "15%"
        salarioReajustado = salarioAtual + aumento

    if salarioAtual > 700 and salarioAtual < 1500:

        aumento = salarioAtual * 0.1 
        percentualAumento = "10%"
        salarioReajustado = salarioAtual + aumento

    if salarioAtual > 1500:

        aumento = salarioAtual * 0.05 
        percentualAumento = "5%"
        salarioReajustado = salarioAtual + aumento

    print("Salário antes do reajuste:", salarioAtual)
    print("Percentual de aumento aplicado:", percentualAumento)
    print("Valor do aumento:", round(aumento, 2))
    print("Novo salário, após o aumento:", round(salarioReajustado, 2))
else:
    print("Informe um salário acima de 0 reais!")