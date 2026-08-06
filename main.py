import sqlite3
from clientes import USERS
from flask import Flask, render_template, url_for
from database import criar_tabelas
from produtos import Products


