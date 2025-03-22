#  Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

numeros = 1

while numeros < 50:
    if not numeros % 2 == 0:
        print(numeros)
    numeros = numeros + 1