# Faça um programa que leia 5 números e informe o maior número.

numeros = []

while len(numeros) < 5:
    num = int(input("Informe um número: "))
    numeros.append(num)

maiorNumero = sorted(numeros, reverse=True)[0]

print(f"O maior número é:\n{maiorNumero}")