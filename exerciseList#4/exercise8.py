# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

while len(numeros) < 5:
    num = int(input("Informe um número: "))
    numeros.append(num)

soma =  sum(numeros)
media = soma / len(numeros)

print(f"A soma dos números é:\n{soma}\nA média dos números é:\n{media}")
