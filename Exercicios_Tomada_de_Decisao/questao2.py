print("Seja bem vind@, digite seu respectivo turno conforme a tabela abaixo: \n"
      "[ M ] Matutino \n"
      "[ V ] Vespertino \n"
      "[ N ] Noturno")
turnos = ["M", "V", "N"]
turno = input("Qual seu turno?  ").upper()

while turno not in turnos:
    print("Valor invalido!")
    print("Digite seu respectivo turno conforme a tabela abaixo: \n"
          "[ M ] Matutino \n"
          "[ V ] Vespertino \n"
          "[ N ] Noturno")
    turno = input("Qual seu turno?  ").upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Invalido!")
   

