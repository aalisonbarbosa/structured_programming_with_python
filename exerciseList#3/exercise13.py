# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = int(input("Digite um número positivo menor que 1000: "))

if numero < 1 or numero > 1000:
    print("Número inválido")
else:
    centenas = numero // 100
    dezenas = (numero - (centenas * 100)) // 10
    unidades = (numero - (centenas * 100) - (dezenas * 10))

    print(numero,"=",centenas,"Centenas,",dezenas,"Dezenas e",unidades,"Unidades")