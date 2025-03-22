# • Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# • F = (C×1.8) + 32

tempCel = float(input("Temperatura em graus celsius: "))
tempFah = (tempCel*1.8) + 32

print("Temperatura em graus fahrenheit: ", round(tempFah, 2))