
import sqlite3

#Criar um banco de dados chamado biblioteca.db

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

# Criar a tabela Livros 

cursor.execute('''
CREATE TABLE IF NOT EXISTS Livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL UNIQUE,
    autor TEXT,
    ano INTEREGER,
    genero TEXT,
    disponivel INTEGER CHECK (disponivel IN (0, 1))
)
''')

# Confira as alterações
conexao.commit()

print("Tabela 'Livros' criada com sucesso!")

# Fecha a conexão
conexao.close()

# Conectar ao banco de dados ( usar biblioteca.bd)

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()
