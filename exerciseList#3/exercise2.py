# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Digite um número: "))

if num > 0:
    print("O número é positivo")
elif num == 0:
    print("O número é neutro")
else: 
    print("O número é negativo")