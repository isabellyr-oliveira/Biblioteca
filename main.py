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
conexao.commit()

def cadastrar_lisvro(titulo,autor,ano):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute(""" 
        INSERT INTO livros(título,autor,ano,disponível)
        VALUES (?,?,?,?)
        """,
        (titulo,autor,ano, "Sim",)
        )
        conexao.commit()
        
        if cursor.rowcount > 0:
            print("O livro foi cadastrado com sucesso!")
        else:
            print("O cadastro do livro não foi concluído.")
    except Exeption as erro:
        print(f"Erro ao tentar cadastrar livro {erro}")
    finally:
        if conexao:
            conexao.close()
            
titulo = input("Digite o título livro de deseja cadastrar: ")
autor = input("Digite o nome do autor do livro que deseja cadastrar: ")
ano = int(input("Digite o ano em que o livro que deseja cadastrar foi publicado: "))

cadastrar_lisvro(titulo,autor,ano)
conexao.commit()

def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"Título: {linha[1]} | Autor: {linha[2]} | Ano: {linha[3]} | Disponibilidade: {linha[4]}")
    except Exeption as erro:
        print(f"Erro ao listar os livros cadastrados {erro}")
    finally:
        if conexao:
            conexao.close()
listar_livros()
conexao.commit()
