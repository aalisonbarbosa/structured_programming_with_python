#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

while True:
    numero = input("Informe um número: ")

    if not numero.isdigit():
        print("Número inválido!")
        continue

    numero = int(numero)

    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"{numero}! = {calculoFatorial} = {fatorial}")
    break