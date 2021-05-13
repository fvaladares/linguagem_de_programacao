import sqlite3

# Cria banco de dados
conn = sqlite3.connect('aulaDB.db')
print(type(conn))

# Cria tabela no banco, pois está dentro da mesma conexão
ddl_create = """
CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT, 
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL
);
"""
cursor = conn.cursor()
cursor.execute(ddl_create)
print("Tabela criada!")

# Insere dados dentro da tabela no mesmo banco, pois está na mesma conexão
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

# Extrai as informações de uma tabela
cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()

print(type(resultado))

for linha in resultado:
    print(linha)

# Fecha o cursor e a conexão
cursor.close()
conn.close()
