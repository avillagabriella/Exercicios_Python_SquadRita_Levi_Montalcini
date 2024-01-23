print("Responda o interrogatório com SIM ou NÃO conforme as perguntas!")

lista_respostas = []
pergunta_1 = input("Primeira pergunta: Telefonou para a vítima? Responda: ")
lista_respostas.append(pergunta_1)
pergunta_2 = input("Segunda pergunta: Esteve no local do crime? Responda: ")
lista_respostas.append(pergunta_2)
pergunta_3 = input("Terceira pergunta: Mora perto da vítima? Responda: ")
lista_respostas.append(pergunta_3)
pergunta_4 = input("Quarta pergunta: Devia para a vítima? Responda: ")
lista_respostas.append(pergunta_4)
pergunta_5 = input("Quinta pergunta: Já trabalhou com a vítima? Responda: ")
lista_respostas.append(pergunta_5)
#print(lista_respostas)
#classificacao = Suspeito (2S), Cúmplice(>=3and<=4), Assassino(5), Inocente(nenhum)

repetivos_positivos = 0
#repetivos_positivos = lista_respostas.count("sim")
#print(repetivos_positivos)

for i in range(len(lista_respostas)):
    if lista_respostas [i] == 'sim':
        repetivos_positivos += 1 
print(repetivos_positivos)
if repetivos_positivos >=3 and repetivos_positivos <= 4:
    print('Cúmplice')
elif repetivos_positivos == 5:
    print('Assassino')
elif repetivos_positivos == 2:
    print('Suspeito')
else:
    print('Inocente')


















