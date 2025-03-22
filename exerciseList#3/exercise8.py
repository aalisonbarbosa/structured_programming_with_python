# Faça um Programa que leia três números e mostre-os em ordem decrescente

numeros = []

while len(numeros) < 3:
    numero = input("Digite um número: ")
    try:
        numero = float(numero)
        numeros.append(numero)
    except:
        print("Digite um número válido.")
print("Os números digitados em ordem decrescente são: ", sorted(numeros, reverse=True))
