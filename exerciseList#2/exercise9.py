# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
# • C = (F−32) ÷ 1.8.

tempFah = float(input("Temperatura em graus fahrenheit: "))
tempCel = ((tempFah - 32) / 1.8)

print("Temperatura em graus celsius: ", round(tempCel, 2))