nome = str(input("Digite seu nome: ").upper())
print(f"Olá {nome}, bem vind@ a calculadora mágica do ENEM!\n"
       "Aqui você vai descobrir qual sua média e uma sugestao em qual aréa sua nota terá maior peso.")

print("Digite a seguir sua nota referente a disciplina:")
ciencias_Nat = float(input("Ciências da Natureza: "))
ciencias_Hum = float(input("Ciências Humanas: "))
linguagens = float(input("Linguagens, Códigos e suas Tecnologias: "))
matematica = float(input("Matemática e suas tecnologias: "))
redacao = float(input("Redação: "))

notas = [ciencias_Nat, ciencias_Hum, linguagens, matematica, redacao]
media = sum(notas) / 5
maior_nota = max(notas)

print(f"Sua média é de {media:.2f}")

if ciencias_Nat == maior_nota:
    print(f"Sua maior nota é em Ciências da Natureza")
elif ciencias_Hum == maior_nota:
    print(f"Sua maior nota é em Ciências Humanas")
elif linguagens == maior_nota:    
    print(f"Sua maior nota é em linguagens, Códigos e suas Tecnologias")
elif matematica == maior_nota: 
    print(f"Sua maior nota é em Matemática e suas tecnologias")
else:
    print(f"Sua maior nota é em Redação")
