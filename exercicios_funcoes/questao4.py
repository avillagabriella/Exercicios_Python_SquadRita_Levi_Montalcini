def converter_para_moedas(valor_na_carteira, conversoes):
    print("\nConversão de R$ {:.2f} reais:".format(valor_na_carteira))
    for moeda, taxa in conversoes.items():
        valor_em_moeda = valor_na_carteira / taxa
        print("{}: R$ {:.2f}".format(moeda, valor_em_moeda))

if __name__ == "__main__":
    conversoes = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suiço": 0.42,
        "Euro": 5.36,
        "Libra esterlina": 6.21
    }

    valor_na_carteira = float(input("Quantos reais você tem na carteira? "))

    converter_para_moedas(valor_na_carteira, conversoes)
