import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect("dados.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    parcela INTEGER NOT NULL,
    preco REAL NOT NULL)
    """)

    cursor.execute("""
    CREARE TABLE IF NOT EXISTS
    produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER NOT NULL)    
        """)
    conexao.commit()
    conexao.close()