# Solicitação de três números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Ordenação dos números em ordem crescente
numeros_ordenados = sorted([num1, num2, num3])

# Apresentação do resultado
print("Números em ordem crescente:", numeros_ordenados)