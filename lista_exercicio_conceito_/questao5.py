salarioBruto = float(input('Digite o valor do salario bruto: '))
aliquotaIR = 0

if (salarioBruto <= 1903.98):
    aliquotaIR = 0
elif (salarioBruto > 1903.98 and salarioBruto <= 2826.65):
    aliquotaIR = 0.075
elif (salarioBruto > 2826.65 and salarioBruto <= 3751.05):
    aliquotaIR = 0.15
elif (salarioBruto > 3751.05 and salarioBruto <= 4664.68):
    aliquotaIR = 0.225
elif (salarioBruto > 4664.68):
    aliquotaIR = 0.275

salarioLiquido = salarioBruto - (salarioBruto*aliquotaIR)

print(f'O salario liquido será de: {salarioLiquido:.2f}')