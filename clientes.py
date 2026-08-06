import sqlite3  

class USERS:
    def __init__(self):
        self.conexao = sqlite3.connect("dados.db")
        self.cursor = self.conexao.cursor()
        self.cursor.execute

    def quitar_parcela(self):
        quitar_nome = input("Digite o nome do cliente que deseja quitar parcelas: ").upper()
        self.cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (quitar_nome,))
        cliente = self.cursor.fetchone()
        if cliente:
            parcelas_quitar = int(input("Digite o número de parcelas a quitar: "))
            if parcelas_quitar <= 0:
                print("Número de parcelas inválido.")
            elif parcelas_quitar > 0 and parcelas_quitar <= cliente[5]:
                self.cursor.execute("UPDATE usuarios SET parcela = ? WHERE nome = ?", (cliente[5] - parcelas_quitar, quitar_nome))
                self.conexao.commit()
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
        self.conexao.commit()

    def encontrar_telefone(self):
        telefone = input("Digite o telefone do cliente que deseja consultar: ")
        self.cursor.execute("SELECT * FROM clientes WHERE telefone = ?", (telefone,))
        cliente = self.cursor.fetchone()
        if cliente:
            print(f"""
            ID: {cliente[0]},
            Nome: {cliente[1]}, 
            Produto: {cliente[2]}, 
            Telefone: {cliente[3]},
            Quantidade: {cliente[4]}, 
            Parcelas: {cliente[5]}, 
            Preço: {cliente[6]}""")
        else:
            print("Usuário não encontrado.")

    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM clientes")
        clientes = self.cursor.fetchall()
        if clientes:
            for cliente in clientes :
                print(f"""
                ID: {cliente[0]},
                Nome: {cliente[1]}, 
                Produto: {cliente[2]}, 
                Telefone: {cliente[3]},
                Quantidade: {cliente[4]}, 
                Parcelas: {cliente[5]}, 
                Preço: {cliente[6]}""")
        else:
            print("Nenhum usuário cadastrado.")
    
    def especifico(self):
        nome_usuario = str(input("Digite o nome do cliente que deseja consultar: ")).lower()
        self.cursor.execute("SELECT * FROM cliente WHERE nome = ?", (nome_usuario,))
        cliente = self.cursor.fetchone()
        if cliente:
            print(f"""
            ID: {cliente[0]},
            Nome: {cliente[1]}, 
            Produto: {cliente[2]}, 
            Telefone: {cliente[3]},
            Quantidade: {cliente[4]}, 
            Parcelas: {cliente[5]}, 
            Preço: {cliente[6]}""")
        else:
            print("Usuário não encontrado.") 
