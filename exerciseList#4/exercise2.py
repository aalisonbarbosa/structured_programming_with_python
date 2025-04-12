# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagemde erro e voltando a pedir as informações.

while True:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    
    if nome == senha:
        print("Sua senha não pode ser igual a seu nome!\nTente novamente!")
        continue
    break