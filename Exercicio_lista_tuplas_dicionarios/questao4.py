contatos = {
    'Manoel Souza': '99999-9999',
    'Cláudia Pinheiro': '98754-6398',
    'Carlos Machado': '8547-9658',
    'Jose Roberto Carvalho': '8974-6985',
}

def procurar_contato(nome):
    if nome in contatos:
        return f"Nome: {nome} - telefone: {contatos[nome]}"
    else:
        return f"Contato não encontrado {nome}"

nome_pesquisa = input("Digite o nome: ")
 
resultado = procurar_contato(nome_pesquisa)
print(resultado)