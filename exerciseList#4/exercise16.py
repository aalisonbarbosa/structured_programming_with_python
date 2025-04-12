# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros = [1,2,3,4,5,6,7,8,9,10]

menorNumero = sorted(numeros)[0]
maiorNumero = sorted(numeros, reverse=True)[0]
somaNumeros = sum(numeros)

print(f"Menor número:\n{menorNumero}\nMaior número:\n{maiorNumero}\nSomas dos números:\n{somaNumeros}")