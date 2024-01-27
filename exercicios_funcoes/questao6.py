import random as rd 
lista = ['AMEIXA', 'ALFACE', 'BANANA', 'CEREAL', 'FAROFA', 'FRANGO', 'JUJUBA', 'PASTEL', 'PIPOCA', 'QUEIJO']

def escolher_palavra_aleatoria(lista):
    tamanho = len(lista)
    sorteio = rd.randint(1,tamanho)
    palavra_aleatoria = lista[sorteio]
    return palavra_aleatoria

palavra_correta = escolher_palavra_aleatoria(lista)


digitadas = []

chances = 6

print('JOGO DA FORCA\n')

while chances <= 6:
    tentativa = input('Digite um letra: ').upper()
    if len(tentativa) > 1:
        print('Erro! Só é possível digitar uma letra por vez!')
        continue
    
    digitadas.append(tentativa)
    
    correta_temporaria = ''

    for letra_secreta in palavra_correta:
        if letra_secreta in digitadas:
            correta_temporaria += letra_secreta
        else:
            correta_temporaria += '*'

    if correta_temporaria == palavra_correta:
        print(f'A palavra correta está assim: {correta_temporaria}')
        print('Você ganhou!')
        break
    else:
        print(f'A palavra correta está assim: {correta_temporaria}')

   
    ver_palpite = input('Deseja dar um palpite? S ou N: ').upper()
    
    while ver_palpite != 'S' and ver_palpite != 'N':
        ver_palpite = input('Por gentileza, digite apenas S ou N: ').upper()   
    

    if ver_palpite == 'S':
        palpite = input('Digite seu palpite: ').upper()

        if palpite == palavra_correta:
            print('Você ganhou!')
            break
        else:
            print('Palpite errado!')     
            continue      
      
    chances -= 1
            
    if chances <= 0:
        print('Que pena, você perdeu!')
        break

    print(f'Você ainda tem {chances} chances.')
    print()