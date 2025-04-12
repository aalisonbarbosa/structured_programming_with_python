#8 Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado: 
# • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
# • A mensagem "Reprovado", se a média for menor do que sete; 
# • A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

mediaNotas = (nota1 + nota2) / 2

if mediaNotas >= 0 and mediaNotas <= 10:
    if mediaNotas == 10:
        print("Aprovado com Distinção")
    elif mediaNotas > 6 and mediaNotas < 10:
        print("Aprovado")
    else: 
        print("Reprovado")
else:
    print("Nota inválida!")