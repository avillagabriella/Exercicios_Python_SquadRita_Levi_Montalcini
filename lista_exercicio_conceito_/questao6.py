distancia = float(input('Digite a distância, em km, que será percorrida: '))

velocidadeAviao = 600
velocidadeCarro = 100
velocidadeOnibus = 80

tempoAviao = distancia/velocidadeAviao
tempoCarro = distancia/velocidadeCarro
tempoOnibus = distancia/velocidadeOnibus

print(f'O tempo de duração da viagem de Avião será de: {tempoAviao}h\n')
print(f'O tempo de duração da viagem de Carro será de: {tempoCarro}h\n')
print(f'O tempo de duração da viagem de Onibus será de: {tempoOnibus}h\n')