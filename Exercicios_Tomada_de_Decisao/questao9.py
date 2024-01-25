# Inicialização de contadores
num_pares = 0
num_impares = 0

# Loop para leitura de números
while True:
    # Solicitação do número ao usuário
    numero = int(input("Digite um número (ou 0 para encerrar): "))

    # Verificação se o número é zero (encerra o loop)
    if numero == 0:
        break

    # Verificação se o número é positivo
    if numero > 0:
        # Contagem de números pares e ímpares
        if numero % 2 == 0:
            num_pares += 1
        else:
            num_impares += 1
    else:
        print("Digite apenas números positivos.")

# Apresentação do resultado
print(f"Quantidade de números pares: {num_pares}")
print(f"Quantidade de números ímpares: {num_impares}")