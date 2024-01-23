print("Ao finalizar o carrinho basta adicionar 'finalizar' a compra.")
carrinho_compras = {}
caixa = "passando"
somaCarrinho = 0
while caixa != "finalizar":
    caixa = input("Adicione produtos ou finalize a compra:")
    if caixa != "finalizar":
        valor = int(input(f"Valor do produto: {caixa}:"))
        carrinho_compras[caixa] = valor
        print(carrinho_compras)
        somaCarrinho += valor
print(f"Compra finalizada! Valor total: R$ {somaCarrinho:.2f}")