alunos = [
    {'nome' : 'Yasmin', 'notas' : [7, 7], 'idade': 16, 'faltas': 30},
    {'nome' : 'Bruno', 'notas' : [7, 8], 'idade': 16, 'faltas': 35},
    {'nome' : 'Ana', 'notas' : [6, 9], 'idade': 15, 'faltas': 50},
    {'nome' : 'Estevan', 'notas' : [9, 8], 'idade': 15, 'faltas': 0},
    {'nome' : 'Eduardo', 'notas' : [6, 7], 'idade': 15, 'faltas': 255},
    {'nome' : 'Rafael', 'notas' : [9, 9], 'idade': 16, 'faltas': 10}

]

def calculaMedia (soma, Qntd):
    return soma/ Qntd

def statusAprovacao (nota, faltas):
    if nota >= 7 and faltas <= 90:
        return print('aprovado')   
    if nota < 7:
        return print('reprovado por nota')
    if faltas > 90:
        return print('reprovado por faltas')

for aluno in alunos:
    Qntd_notas = len(aluno['notas'])
    soma = sum(aluno['notas'])
    nota = calculaMedia(soma, Qntd_notas)
    print(f"Aluno: {aluno['nome']}, média: {nota}")
    statusAprovacao(nota, aluno['faltas'])
