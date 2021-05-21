import sqlite3
from datetime import date, datetime

# Cria banco de nomes
conn = sqlite3.connect('aulaDB.db')
print(type(conn))


def imprimir_lista(resultSet, origem_dados):
    print('-' * 10)
    print(f'Dados do {origem_dados}')
    for resultado in resultSet:
        print(resultado)


# # Cria tabela no banco, pois está dentro da mesma conexão
# ddl_create = """
# CREATE TABLE fornecedor (
#     id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     nome_fornecedor TEXT NOT NULL,
#     cnpj VARCHAR(18) NOT NULL,
#     cidade TEXT,
#     estado VARCHAR(2) NOT NULL,
#     cep VARCHAR(9) NOT NULL,
#     data_cadastro DATE NOT NULL
# );
# """


# criando a tabela (schema)
# ddl_create = """
#     CREATE TABLE clientes (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             nome TEXT NOT NULL,
#             idade INTEGER,
#             cpf     VARCHAR(14) NOT NULL,
#             email TEXT NOT NULL,
#             fone TEXT,
#             cidade TEXT,
#             uf VARCHAR(2) NOT NULL,
#             criado_em DATE NOT NULL
#     );
# """


cursor = conn.cursor()
# cursor.execute(ddl_create)
print("Tabela criada!")

# Insere nomes dentro da tabela no mesmo banco, pois está na mesma conexão
cursor.execute("""
    INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
    VALUES ('Empresa A', '11.111.111/1111-11', 'São Paulo', 'SP', '11111-111', '2020-01-01')
""")

cursor.execute("""
    INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
    VALUES ('Empresa B', '22.222.222/2222-22', 'Rio de Janeiro', 'RJ', '22222-222', '2020-01-01')
""")

cursor.execute("""
    INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
    VALUES ('Empresa C', '33.333.333/3333-33', 'Curitiba', 'PR', '33333-333', '2020-01-01')
""")

cursor.execute("""
    INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
    VALUES ('Empresa D', '44.444.444./4444-44', 'Belo Horizonte', 'MG', '33600-000', '2021-05-13')
""")

conn.commit()
data = date.today()
print(f'Data: {data}')
queue = f"""
    INSERT INTO clientes 
    ( nome, idade, cpf, email, fone, cidade, uf, criado_em )
    VALUES 
    ( 'Fabricio Valadares', 39, '111.222.333-44', 'fabricio.valadares@pitagoras.com.br', 
    '31993576193', 'Pedro Leopoldo', 'MG', \'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\') 
"""

print(f'Queue: {queue}')

cursor.execute(queue)
conn.commit()

# Extrai as informações de uma tabela
cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()
imprimir_lista(resultado, 'fornecedor all')

cursor.execute("""
    SELECT * FROM fornecedor WHERE cidade = 'Belo Horizonte' AND id_fornecedor > 10
""")
resultado = cursor.fetchall()
imprimir_lista(resultado,
               "fornecedor filtrado  SELECT * FROM fornecedor WHERE cidade = 'Belo Horizonte' AND id_fornecedor > 10")

cursor.execute("""
    SELECT * FROM clientes
""")
resultado = cursor.fetchall()
imprimir_lista(resultado, 'clientes all SELECT * FROM clientes')

# Fecha o cursor e a conexão
cursor.close()
conn.close()
