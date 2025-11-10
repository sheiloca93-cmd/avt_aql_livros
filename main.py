
import sqlite3


# Dados para inserir
livros = [
    ('Dom Almeida', 'Amélia Santos', '1988', 'Romance', 1),
    ('A vida de Alice', 'Bento Costa', '1940', 'Ficção', 1),
    ('O mistério da casa ao lado', 'Clara Machado', '2020', 'Suspense', 0),
    ('Quanto mais risos melhor', 'Lorena Sanchez', '1945', 'Comédia', 1),
    ('Revolução do Brasil', 'Paulo Freitas', '1899', 'Distopia', 0),
]


# Inserindo livros


# Confirma as alterações
conexao.commit()

print("Livros inseridos com sucesso!")

# Fecha a conexão
conexao.close() 

import sqlite3

# Conecta ao banco de dados

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()