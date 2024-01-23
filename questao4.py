contatos = [
    {"nome": "Alice", "telefone": "7439702"},
    {"nome": "José", "telefone": "7439542"},
    {"nome": "Maria", "telefone": "3439702"},
    {"nome": "João", "telefone": "74391111"},
    {"nome": "Matheus", "telefone": "78499702"}
]

nome = input("Procurar por nome: ")
contato_encontrado = None
for contato in contatos:
    if contato["nome"] == nome:
        contato_encontrado = contato
        break

if contato_encontrado:
    telefone = contato_encontrado["telefone"]
    print(f"Nome: {nome}, Telefone: {telefone}")
else:
    print(f"Contato com o nome {nome} não encontrado.")