import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(cursor):
    cursor.execute(
        'CREATE TABLE clientes ' \
        'id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
        'nome VARHAR(100), ' \
        'email VARCHAR(100)' \
        ')')
    conexao.commit()

def inserir_registros(conexao,cursor,nome,email):
    data = (nome,email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);",data)
    conexao.commit()

def atualizar_registros(conexao,cursor,nome,email,id):
    data = (nome,email,id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;',data)
    conexao.commit()

def excluir_registros(conexao,cursor,id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;',data)
    conexao.commit()

# atualizar_registros(conexao,cursor,"Danyelle","danyelle@gmail.com",1)
# excluir_registros(conexao,cursor,1)

def inserir_muitoss(conexao,cursor,dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()

# dados = [
#     ("Dany","dany@gmail.com"),
#     ("Gabri","gabri@gmail.com"),
#     ("João","jao@gmail.com"),
#     ("Jose","ze@gmail.com"),
# ]

# inserir_muitoss(conexao,cursor,dados)

def recuperar_cliente(cursor,id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

cliente = recuperar_cliente(cursor,2)
print(dict(cliente))
print(cliente["id"],cliente["nome"],cliente["email"])

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")

# clientes = listar_clientes(cursor)
# for cliente in clientes:
#     print(dict(cliente))

