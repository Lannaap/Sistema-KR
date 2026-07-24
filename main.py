import sqlite3

conexion = sqlite3.connect("dados-l.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    parcela INTEGER NOT NULL,
    preco REAL NOT NULL
)""")



def cadastroc():

    nome = input("Digite o nome completo do cliente: ").upper()
    produto = input("Digite o produto: ").upper()    
    quantidade = int(input("Digite a quantidade: "))
    parcela = int(input("Digite o número de parcelas: "))
    preco = float(input("Digite o preço: "))

    cursor.execute("INSERT INTO usuarios (nome, produto, quantidade, parcela, preco) VALUES (?, ?, ?, ?, ?)", (nome, produto, quantidade, parcela, preco))
    conexion.commit()

def listar_usuarios():
    
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(f" Nome: {usuario[1]}")

def especifico():
    nome_usuario = input("Digite o nome do cliente que deseja consultar: ").upper()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome_usuario,))
    usuario = cursor.fetchone()
    if usuario:
        print(f"""
        ID: {usuario[0]},
        Nome: {usuario[1]}, 
        Produto: {usuario[2]}, 
        Quantidade: {usuario[3]}, 
        Parcelas: {usuario[4]}, 
        Preço: {usuario[5]}""")
    else:
        print("Usuário não encontrado.")

print("Bem-vindo ao sistema de cadastro de clientes!")

while True:
    print("\n1. Cadastrar cliente")
    print("2. Listar todos os clientes")
    print("3. Consultar cliente específico")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastroc()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        especifico()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
