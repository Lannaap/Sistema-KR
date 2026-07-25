import sqlite3

conexion = sqlite3.connect("dados-l.db")
cursor = conexion.cursor()
#0 = id, 1 = nome, 2 = telefone, 3 = produto, 4 = quantidade, 5 = parcela, 6 = preco
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT UNIQUE NOT NULL,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    parcela INTEGER NOT NULL,
    preco REAL NOT NULL
)""")

def quitar_parcela():
    quitar_nome = input("Digite o nome do cliente que deseja quitar parcelas: ").upper()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (quitar_nome,))
    usuario = cursor.fetchone()
    if usuario:
        parcelas_quitar = int(input("Digite o número de parcelas a quitar: "))
        if parcelas_quitar <= 0:
            print("Número de parcelas inválido.")
        elif parcelas_quitar > 0 and parcelas_quitar <= usuario[5]:
            cursor.execute("UPDATE usuarios SET parcela = ? WHERE nome = ?", (usuario[5] - parcelas_quitar, quitar_nome))
            conexion.commit()
            print("Parcelas quitadas com sucesso.")
        else:
            print("Número de parcelas inválido.")
    else:
        print("Usuário não encontrado.")

def cadastroc():

    while True:

        telefone = input("Digite o telefone do cliente: ").upper()
        if len(telefone) == 11 and telefone.isdigit():
            break
        print("O telefone deve conter exatamente 11 números.")

        nome = input("Digite o nome do cliente: ").upper()
        produto = input("Digite o produto: ").upper()
        quantidade = int(input("Digite a quantidade do produto: "))
        parcela = int(input("Digite o número de parcelas: "))
        preco = float(input("Digite o preço do produto: "))

    cursor.execute("INSERT INTO usuarios (nome, telefone, produto, quantidade, parcela, preco) VALUES (?, ?, ?, ?, ?, ?)", (nome, telefone, produto, quantidade, parcela, preco))
    conexion.commit()

def encontrar_telefone():
    telefone = input("Digite o telefone do cliente que deseja consultar: ")
    cursor.execute("SELECT * FROM usuarios WHERE telefone = ?", (telefone,))
    usuario = cursor.fetchone()
    if usuario:
        print(f"""
        ID: {usuario[0]},
        Nome: {usuario[1]}, 
        Produto: {usuario[2]}, 
        Telefone: {usuario[3]},
        Quantidade: {usuario[4]}, 
        Parcelas: {usuario[5]}, 
        Preço: {usuario[6]}""")
    else:
        print("Usuário não encontrado.")

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    if usuarios:
        for usuario in usuarios:
            print(f"""
            ID: {usuario[0]},
            Nome: {usuario[1]}, 
            Produto: {usuario[2]}, 
            Telefone: {usuario[3]},
            Quantidade: {usuario[4]}, 
            Parcelas: {usuario[5]}, 
            Preço: {usuario[6]}""")
    else:
        print("Nenhum usuário cadastrado.")
 
def especifico():
    nome_usuario = str(input("Digite o nome do cliente que deseja consultar: ")).lower()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome_usuario,))
    usuario = cursor.fetchone()
    if usuario:
        print(f"""
        ID: {usuario[0]},
        Nome: {usuario[1]}, 
        Produto: {usuario[2]}, 
        Telefone: {usuario[3]},
        Quantidade: {usuario[4]}, 
        Parcelas: {usuario[5]}, 
        Preço: {usuario[6]}""")
    else:
        print("Usuário não encontrado.")

print("Bem-vindo ao sistema de cadastro de clientes!")

while True:
    print("\n1. Cadastrar cliente")
    print("2. Listar todos os clientes")
    print("3. Consultar cliente específico")
    print("4. Consultar cliente por telefone")
    print("5. Quitar parcelas de um cliente")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastroc()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        especifico()
    elif opcao == "4":
        encontrar_telefone()
    elif opcao == "5":
        quitar_parcela()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
