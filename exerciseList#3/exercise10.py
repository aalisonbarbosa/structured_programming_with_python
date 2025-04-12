# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

diasSemana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

while True:
    dia = int(input("Digite um número de 1 a 7: "))
    
    if dia > 0 and dia < 8:
        print("Dia da semana correspondente:", diasSemana[dia - 1])
    else:
        print("Número inválido!")
        continue
    break