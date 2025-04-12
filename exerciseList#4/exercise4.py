# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a populaçãode B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacaoA = 80000
populacaoB = 200000

taxaCrescimentoPopulacaoA = 1.03
taxaCrescimentoPopulacaoB = 1.015

anosNecessarios = 0

while populacaoA < populacaoB:

    anosNecessarios = anosNecessarios + 1

    populacaoA = populacaoA * taxaCrescimentoPopulacaoA
    populacaoB = populacaoB * taxaCrescimentoPopulacaoB

print("O número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B:")
print(f"{anosNecessarios} anos.")