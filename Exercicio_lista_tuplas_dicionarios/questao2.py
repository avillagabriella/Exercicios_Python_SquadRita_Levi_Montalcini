contador = 1
qtdAlunos = 0
medias = []
while contador <=5:
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    nota3 = float(input('Digite a terceira nota do aluno: '))
    nota4 = float(input('Digite a quarta nota do aluno: '))

    media = (nota1+nota2+nota3+nota4)/4

    if media >= 7:
        medias.append(media)
        qtdAlunos += 1
    
    contador+=1

print(f'O numero de alunos com media maior ou igual a 7 foi de: {qdtAlunos}')
print(medias)