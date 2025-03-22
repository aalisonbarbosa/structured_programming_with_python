# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

num = 1
lista = ""

while num <= 20:

    print(num)
    
    if num == 20:
        lista = lista + (f"{num}.")
    else:
        lista = lista + (f"{num}, ")

    num = num + 1

print(f"\n{lista}")