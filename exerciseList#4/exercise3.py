# Faça um programa que leia e valide as seguintes informações:
# • Nome: maior que 3 caracteres;
# • Idade: entre 0 e 150;
# • Salário: maior que zero;
# • Sexo: 'f' ou 'm';
# • Estado Civil: 's', 'c', 'v', 'd’

while True:
    nome = input("Digite seu nome: ")

    if len(nome) < 4:
        print("Digite um nome maior que 3 caracteres")
    else:
        break

while True:
    idade = int(input("Digite sua idade: "))

    if idade < 0 or idade > 150:
        print("Informe uma idade entre 0 e 150 anos")
    else:
        break

while True:
    salario = float(input("Informe seu salário: "))

    if salario < 0:
        print("Informe um salário válido")
    else:
        break

while True:
    sexo = input("Informe seu sexo: f ou m ")

    if not sexo in "FMfm":
        print("Informe um sexo válido")
    else:
        break

while True:
    estadoCivil = input("Informe seu estado civil\nEstado Civil: 's', 'c', 'v', 'd’: ")
    
    if not estadoCivil in 'SCVDscvd':
        print("Informe um estado civil válido")
    else:
        break