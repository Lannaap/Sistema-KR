import sqlite3

class Products: 

    def __init__(self):
        self.conexao = sqlite3.connect("dados.db")
        self.cursor = self.conexao.cursor()

    def cadastro_p(self):
        nome_p = input("Digite o nome do produto: ")
        preco_p = input("Digite o preço do produto: ")
        qte_est = input("Digite a quantidade em estoque")

        self.cursor.execute(
            "INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)",
            (nome_p, preco_p, qte_est))
        self.conexao.commit()

    def estoque(self):
        self.cursor.execute("SELECT * FROM produtos")
        produto = self.cursor.fetchall()

        if produtos:
            for produtos in produto:
                print(f""" 
                produto: {produto[1]}, 
                preco: {produto[2]},  
                estoque: {produto[3]}""")

    def excluir(self, nome_p):
        self.cursor.execute(
            "DELETE FROM produtos WHERE nome = ?",
            (nome_p,))
        self.conexao.commit()
