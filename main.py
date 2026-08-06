import sqlite3
from produtos import Products
from clientes import USERS
from flask import Flask, render_template, url_for
from database import criar_tabelas
from produtos import Products

produtos = Products()
cliente = USERS()


print ("Bem vindo ao sistema KR")
print("O que deseja fazer")
print("Configuração de produtos [1]\nConfigutação de clientes[2]")

escolha = input("Digite a escolha: ")

if escolha == 1: #escolha produtos

    print("O que deseja fazer?")
    print("Cadastrar produtos [1]\n "
    "Consultar estoque [2]\n " \
    "Atualizar estoque [3]\n " \
    "Excluir de produtos [4]")

    escolha_p = input("Digite o que deseja fazer: ")
    if escolha_p == 1:
        produtos.cadastro_p()
    elif escolha_p == 2:
        produtos.estoque()
    elif escolha_p == 4:
        produtos.excluir()

elif escolha == 2: #escolha clientes
        print("O que deseja fazer?")
        print("Cadastar Clientes [1]\n "
        "Consultar/listar clientes [2]\n " \
        "Atualizar parcela [3]\n " \
        "Excluir clientes [4]\n" \
        "Listar cliente especifico[5]\n" \
        "Encontrar por telefone[6]")

        escolha_c = input("Digite o que deseja fazer: ")
        if escolha_c == 1:
            cliente.cadastroc()
        elif escolha_c == 2:
            cliente.listar_usuarios()
        elif escolha_c == 3:
            cliente.quitar_parcela()
        elif escolha_c == 4:
             print("nao fiz rs")
        elif escolha_c == 5:
             cliente.listar_usuarios()
        elif escolha_c ==   6:
             cliente.encontrar_telefone