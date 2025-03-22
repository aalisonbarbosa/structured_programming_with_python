# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# • Calcule e mostre o total do seu salário no referido mês.

ganhoHora = float(input("Ganho por hora: "))
HorasTrabalhadas = float(input("Horas trabalhadas no mês: "))

SalarioMes = ganhoHora * HorasTrabalhadas

print("Sálario por mês: R$", SalarioMes)