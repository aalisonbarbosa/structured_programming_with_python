# Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é: ", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("O maior número é: ", numero2)
else:
    print("O maior número é: ", numero3) 

if numero1 < numero2 and numero1 < numero3:
    print("O menor número é: ", numero1)
elif numero2 < numero1 and numero2 < numero3:
    print("O menor número é: ", numero2)
else:
    print("O menor número é: ", numero3)   