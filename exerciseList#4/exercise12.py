# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo

while True:
    numero = input("Informe um número: ")

    if not numero.isdigit():
        print("Informe um número válido")
        continue
    
    numero = int(numero)

    if numero < 1 or numero > 10:
        print("Informe um número entre 1 e 10")
        continue
    
    multiplicador = 0

    while multiplicador <= 10:

        resultadoTabuada = numero * multiplicador

        tabuada = (f"{numero} x {multiplicador} = {resultadoTabuada}")

        print(tabuada)
        
        multiplicador = multiplicador + 1
    break