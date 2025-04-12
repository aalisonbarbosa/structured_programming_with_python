# • 6) Crie um método que receba as notas e retorne a média de notas do aluno

notas = [8, 7.5, 8.2]

def analisarNotas(notas):
    mediaNotas = sum(notas)/len(notas)

    return mediaNotas

print(analisarNotas(notas))