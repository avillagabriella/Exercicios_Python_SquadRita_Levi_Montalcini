def CpF():
    temp = float(input("Adicione a temperatura (graus): "))
    f = temp * 1.8 + 32
    print(f"A temperatura em Fahrenheit é: {f}")


def FpC():
    temp = float(input("Adicione a temperatura (Fahrenheit): "))
    c = (temp - 32)/1.8
    print(f"A temperatura em graus  é: {c}")


def mudarTemperatura():
    print("Escolha 1 para converter a temperatura de Celsius para Fahrenheit")
    print("Escolha 2 para converter de Fahrenheit para Celsius")  
    resposta = int(input("Escolha a opção: "))
    if resposta == 1:
        CpF()
    elif resposta == 2:
        FpC()
    else:
        print("Escolha um dos dois números!")
