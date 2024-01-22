print("Vamos calcular seu índice de massa corporal (IMC)!")

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f"Seu indíce é {imc:.2f} - Abaixo do peso!")
elif imc >= 18.6 and imc <= 24.9:
    print(f"Seu indíce é {imc:.2f} - Peso normal!")
elif imc >= 25 and imc <= 29.9:
    print(f"Seu indíce é {imc:.2f} - Sobrepeso!")
elif imc >= 30 and imc <= 34.9:
    print(f"Seu indíce é {imc:.2f} - Obesidade grau I!")
elif imc >= 35 and imc <= 39.9:
    print(f"Seu indíce é {imc:.2f} - Obesidade grau II!")
else:
    print(f"Seu indíce é {imc:.2f} - Obesidade grau III")