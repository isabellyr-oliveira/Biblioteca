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
    except Exception as erro:
        print(f"Erro ao tentar cadastrar livro {erro}")
    finally:
        if conexao:
            conexao.close()


def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"ID: {linha[0]} Título: {linha[1]} | Autor: {linha[2]} | Ano: {linha[3]} | Disponibilidade: {linha[4]}")
    except Exeption as erro:
        print(f"Erro ao listar os livros cadastrados {erro}")
    finally:
        if conexao:
            conexao.close()

def atualizacao_disponibilidade(id_livro,disponivel):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute("""
        UPDATE livros
        SET disponível = ?
        WHERE id = ?          
        """,(disponivel, id_livro)
        )
        conexao.commit()
    except Exception as erro:
        print("Não foi possível fazer a atualização {erro}")
    finally:
        if conexao:
            conexao.close()


def remover_livro(id_livro):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conexao.commit()
        
        if cursor.rowcount > 0:
            print("Livro removido com sucesso!")
        else:
            print("Nenhum livro foi encontrado com o ID fornecido.")
    except Exception as erro:
        print(f"Erro ao tentar excluir livro {erro}")
    finally:
        if conexao:
            conexao.close()




def menu():
    while True:
        print("1 - Cadastrar")
        print("2 - Listar livros")
        print("3 - Atualizar disponibilidade")
        print("4 - Remover livro")
        print("5 - Sair")
        
        opcao = input("Digite uma opçao: ")
        
        if opcao == "1":
            titulo = input("Digite o título livro de deseja cadastrar: ")
            autor = input("Digite o nome do autor do livro que deseja cadastrar: ")
            ano = int(input("Digite o ano em que o livro que deseja cadastrar foi publicado: "))
            cadastrar_lisvro(titulo,autor,ano)
            
        elif opcao == "2":
            listar_livros()
            
        elif opcao == "3":
            livro_id = input("Digite o ID do livro que deseja atualizar: ")
            disponibilidade = input("Atualize a disponibilidade do livro: ")
            atualizacao_disponibilidade(livro_id, disponibilidade)  
        
        elif opcao == "4":
            deletar = int(input("Digite o ID do livro que deseja deletar: "))
            remover_livro(deletar)
        
        elif opcao == "5":
            print("Você saiu do menu!")
            break
menu()   
 