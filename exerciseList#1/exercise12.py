#12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos deve obedecer à tabela acima.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
mediaNotas = (nota1 + nota2) / 2

if mediaNotas >= 0 and mediaNotas <= 10:
    if mediaNotas > 9 and mediaNotas <= 10:
        conceito = "A"
    elif mediaNotas > 7.5 and mediaNotas <= 9:
        conceito = "B"
    elif mediaNotas > 6 and mediaNotas <= 7.5:
        conceito = "C"
    elif mediaNotas > 4 and mediaNotas <= 6:
        conceito = "D"
    else:
        conceito = "E"
        
    print(conceito)
else:
    print("Nota inválida!")