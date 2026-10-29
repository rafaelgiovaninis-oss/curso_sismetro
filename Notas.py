alunos = [
    {'nome' : 'Yasmin', 'notas' : [7, 7], 'idade': 16, 'faltas': 30},
    {'nome' : 'Bruno', 'notas' : [7, 8], 'idade': 16, 'faltas': 35},
    {'nome' : 'Ana', 'notas' : [6, 9], 'idade': 15, 'faltas': 500},
    {'nome' : 'Estevan', 'notas' : [9, 8], 'idade': 15, 'faltas': 0},
    {'nome' : 'Eduardo', 'notas' : [6, 7], 'idade': 15, 'faltas': 255},
    {'nome' : 'Rafael', 'notas' : [9, 9], 'idade': 16, 'faltas': 10},
    {'nome' : 'Arthur', 'notas' : [8, 8], 'idade': 16, 'faltas': 90},
    {'nome' : 'Guilherme', 'notas' : [5, 6], 'idade': 15, 'faltas': 100}

]

alunosAprovados = []
alunosReprovados = []

def calculaMedia (soma, Qntd):
    return soma/ Qntd

def statusAprovacao (nota, faltas):
    if nota >= 7 and faltas <= 90:
        return "aprovado"   
    if nota < 7:
        return "reprovado por nota"
    if faltas > 90:
        return "reprovado por faltas"

for aluno in alunos:
    Qntd_notas = len(aluno['notas'])
    soma = sum(aluno['notas'])
    nota = calculaMedia(soma, Qntd_notas)
    status = statusAprovacao(nota, aluno['faltas'])
    if status == "aprovado":
        alunosAprovados.append(aluno)
    else:
        alunosReprovados.append(aluno)

for aluno in alunosAprovados:
    print(f"Aluno: {aluno['nome']}, Status: Aprovado, Média: {calculaMedia(sum(aluno['notas']), len(aluno['notas']))}, Faltas: {aluno['faltas']}")

for aluno in alunosReprovados:
    print(f"Aluno: {aluno['nome']}, Status: Reprovado, Média: {calculaMedia(sum(aluno['notas']), len(aluno['notas']))}, Faltas: {aluno['faltas']}")
