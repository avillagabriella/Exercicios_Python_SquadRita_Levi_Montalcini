def contar_vogais(frase):
    vogais = 'aeiou'
    total = 0
    for char in frase.lower():
        if char in vogais:
            total += 1
    return total

frase = input("Digite uma frase: ")
total_vogais = contar_vogais(frase)
print("A frase tem {} vogais.".format(total_vogais))