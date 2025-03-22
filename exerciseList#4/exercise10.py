# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles

while True:
    numero1 = input("Informe um número: ") 
    numero2 = input("Informe um número: ")

    if not numero1.isdigit() or not numero2.isdigit():
        print("Número inválido!")
        continue
    
    numero1, numero2 = int(numero1), int(numero2)

    break

intervalo = ""
# numero1 + 1 serve para o range começar pelo próximo número depois do numero1
for num in range(numero1 + 1, numero2):
    intervalo = intervalo + (f"{num} ")
print(f"Intervalo entre os números:\n{intervalo}")