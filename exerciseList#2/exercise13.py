# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintesfórmulas: 
# • Para homens: (72.7*h) –58 
# • Para mulheres: (62.1*h) -44.7

while True:
    altura = float(input("Informe sua altura(metros): "))
    sexo = int(input("Opções:\n1) Feminino\n2) Masculino\nInforme seu sexo: "))
    if sexo == 1:
        pesoIdeal = (72.7*altura) - 58
    elif sexo == 2:
        pesoIdeal = (62.1*altura) - 44.7
    else: 
        print("Opção inválida!")
        continue

    print("Seu peso ideal é: ", round(pesoIdeal, 2), "kg")
    break