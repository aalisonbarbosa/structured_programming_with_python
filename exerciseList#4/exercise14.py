# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = []

while len(numeros) <= 10:
    num = input("Informe um número: ")

    if not num.isdigit():
        print("Número inválido!")
        continue

    num = int(num)
    numeros.append(num)

quantidadeNumerosImpares = 0
quantidadeNumerosPares = 0

for numero in numeros:
    if numero % 2 == 0:
        quantidadeNumerosPares = quantidadeNumerosPares + 1
    else:
        quantidadeNumerosImpares = quantidadeNumerosImpares + 1

print(f"Quantidade de números pares:\n{quantidadeNumerosPares}\nQuantidade de números impares:\n{quantidadeNumerosImpares}")