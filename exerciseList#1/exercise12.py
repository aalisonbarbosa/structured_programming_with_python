#12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos deve obedecer à tabela acima.

media = (float(input("Nota 1: ")) + float(input("Nota 2: "))) / 2

if media >= 0 and media <= 10:
    if media > 9 and media <= 10:
        conceito = "A"
    elif media > 7.5 and media <= 9:
        conceito = "B"
    elif media > 6 and media <= 7.5:
        conceito = "C"
    elif media > 4 and media <= 6:
        conceito = "D"
    else:
        conceito = "E"
        
    print(conceito)
else:
    print("Nota inválida!")