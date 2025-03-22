#8 Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado: 
# • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
# • A mensagem "Reprovado", se a média for menor do que sete; 
# • A mensagem "Aprovado com Distinção", se a média for igual a dez.

media = (int(input("Nota 1: ")) + int(input("Nota 2: "))) / 2

if media >= 0 and media <= 10:
    if media == 10:
        print("Aprovado com Distinção")
    elif media > 6 and media < 10:
        print("Aprovado")
    else: 
        print("Reprovado")
else:
    print("Nota inválida!")