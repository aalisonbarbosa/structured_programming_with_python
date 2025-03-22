# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é: 
# par ou ímpar;
# positivo ou negativo; 
# inteiro ou decimal.

while True:
    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")

    # Verifica se os números são válidos
    if not numero1.isdigit() or not numero2.isdigit():
        print("Números inválidos!")
        continue

    operacao = input("Digite a operação desejada (+, -, *, /): ")

    resultado = eval(numero1 + operacao + numero2)

    print("O resultado da operação é:", resultado)

    # Verifica se o resultado é par ou ímpar
    if resultado % 2 == 0:
        print("O resultado é par.")
    else:
        print("O resultado é ímpar.")
    
    # Verifica se o resultado é positivo ou negativo
    if resultado < 0:
        print("O resultado é negativo.")
    else:
        print("O resultado é positivo.")

    # Verifica se o resultado é inteiro ou decimal
    if round(resultado) == resultado:
        print("O resultado é inteiro.")
    else:
        print("O resultado é decimal.")
    break