# • 6) Crie um método que receba as notas e retorne a média de notas do aluno

notas = [8, 7.5, 8.2]

def analisarNotas(nota):
    media = sum(nota)/len(nota)

    return media

print(analisarNotas(notas))
