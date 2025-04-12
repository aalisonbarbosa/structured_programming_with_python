# Altere o programa anterior para mostrar no final a soma dos números.

while True:
    numero1 = input("Informe um número: ") 
    numero2 = input("Informe um número: ")

    if not numero1.isdigit() or not numero2.isdigit():
        print("Número inválido!")
        continue
    
    numero1, numero2 = int(numero1), int(numero2)

    break

intervaloNumeros = ""
somaNumeros = 0

for num in range(numero1 + 1, numero2):
    intervaloNumeros = intervaloNumeros + (f"{num} ")
    somaNumeros = somaNumeros + num

print(f"Intervalo entre os números:\n{intervaloNumeros}\nSoma do intervalo entre os números:\n{somaNumeros}")