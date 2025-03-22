#10 Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

numero1, numero2 = numero2, numero1

print(numero1)
print(numero2)