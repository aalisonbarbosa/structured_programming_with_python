# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

while True:
    base = input("Informe um número base: ")
    expoente = input("Informe um expoente: ")

    if not base.isdigit() or not expoente.isdigit():
        print("Informe números válidos!")
        continue

    base, expoente = int(base), int(expoente)

    resultado = base ** expoente

    print(f"{base} ** {expoente} =  {resultado}")
    break