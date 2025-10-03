import sqlite3


def criar_tabela():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            título TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            disponível TEXT
        )
        """)
    except Exception as erro:
        print(f"Erro ao tentar criar tabela {erro}")
    finally:
        if conexao:
            conexao.close()   
criar_tabela()