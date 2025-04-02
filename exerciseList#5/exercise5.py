# • 5) Crie um método que receba as notas e retorne a maior nota do aluno

notas = [8, 7.5, 8.2]

def analisarNotas(nota):
    maiorNota = sorted(nota, reverse=True)[0]

    return maiorNota

print(analisarNotas(notas))
