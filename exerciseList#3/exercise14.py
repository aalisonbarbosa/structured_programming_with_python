# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina. 
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = int(input("Digite o valor do saque: "))

if valor < 10 or valor > 600:
    print("Valor inválido")
else:
    nota100 = valor // 100
    nota50 = (valor - (nota100 * 100))//50
    nota10 =(valor - (nota100 * 100) - (nota50 * 50))//10
    nota5 = (valor - (nota100 * 100) - (nota50 * 50) - (nota10 * 10))//5
    nota1 = (valor - (nota100 * 100) - (nota50 * 50) - (nota10 * 10) - (nota5 * 5))

    print("Notas de 100:",nota100)
    print("Notas de 50:",nota50)
    print("Notas de 10:",nota10)
    print("Notas de 5:",nota5)
    print("Notas de 1:",nota1)