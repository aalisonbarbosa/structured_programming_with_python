# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
# • salário bruto. 
# • quanto pagou ao INSS. 
# • quanto pagou ao sindicato. 
# • o salário líquido. 
# • calcule os descontos e o salário líquido, conforme a tabela à direita.

ganhoHora = float(input("Informe quanto ganha por hora: "))
horasTrabalhadasMes = float(input("Informe quantas horas trabalhou no mês: "))

salarioBruto = ganhoHora * horasTrabalhadasMes

print("+ Salário Bruto : R$", salarioBruto)
print("- IR (11%) : R$", salarioBruto * 0.11)
print("- INSS (8%) : R$", salarioBruto * 0.08)
print("- Sindicato (5%) : R$", salarioBruto * 0.05)
print("= Salário líquido : R$", salarioBruto * 0.76)