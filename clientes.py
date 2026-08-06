import sqlite3  

class clientes():
    def __init__(self):
        self.conexao = sqlite3.connect("dados.db")
        self.cursor = self.conexao.cursor()

    def quitar_parcela(self):
        quitar_nome = input("Digite o nome do cliente que deseja quitar parcelas: ").upper()
        self.cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (quitar_nome,))
        usuario = self.cursor.fetchone()
        if usuario:
            parcelas_quitar = int(input("Digite o número de parcelas a quitar: "))
            if parcelas_quitar <= 0:
                print("Número de parcelas inválido.")
            elif parcelas_quitar > 0 and parcelas_quitar <= usuario[5]:
                self.cursor.execute("UPDATE usuarios SET parcela = ? WHERE nome = ?", (usuario[5] - parcelas_quitar, quitar_nome))
                self.conexion.commit()
                print("Parcelas quitadas com sucesso.")
            else:
                print("Número de parcelas inválido.")
        else:
            print("Usuário não encontrado.")

    def cadastroc(self):

        while True:

            telefone = input("Digite o telefone do cliente: ").upper()
            if len(telefone) == 11 and telefone.isdigit():
                break
            print("O telefone deve conter exatamente 11 números.")

        nome = input("Digite o nome do cliente: ").upper()
        produtos = []
        while True:
            produto = input("Digite o produto: ").upper()
            produtos.append(produto)

            mais = input("Deseja adicionar outro produto? (S/N): ").upper()
            if mais == "N":
                break
            elif mais != "S":
                print("Opção inválida. Digite 'S' para sim ou 'N' para não.")

        parcela = int(input("Digite o número de parcelas: ")) 
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        
        self.cursor.execute("INSERT INTO usuarios (nome, telefone, produto, quantidade, parcela, preco) VALUES (?, ?, ?, ?, ?, ?)", (nome, telefone, produto, quantidade, parcela, preco))
        self.conexion.commit()

    def encontrar_telefone(self):
        telefone = input("Digite o telefone do cliente que deseja consultar: ")
        self.cursor.execute("SELECT * FROM usuarios WHERE telefone = ?", (telefone,))
        usuario = self.cursor.fetchone()
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

    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        usuarios = self.cursor.fetchall()
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
    
    def especifico(self):
        nome_usuario = str(input("Digite o nome do cliente que deseja consultar: ")).lower()
        self.cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome_usuario,))
        usuario = self.cursor.fetchone()
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