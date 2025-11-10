
import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

# Mostrar todos os livros para o usuário escolher
cursor.execute('SELECT id, titulo, disponivel FROM Livros')
livros = cursor.fetchall()

print("ista de Livros:")
for livro in livros:
    id, titulo, disponivel = livro
    status = "Disponível" if disponivel == 1 else "Indisponível"
    print(f"{id} - {titulo} ({status})")

# Pedir o ID do livro a ser atualizado
id_livro = int(input("\nDigite o ID do livro que deseja alterar: "))

# Verificar status atual do livro
cursor.execute('SELECT disponivel FROM Livros WHERE id = ?', (id_livro,))
resultado = cursor.fetchone()

if resultado:
    disponivel_atual = resultado[0]
    # Inverter o valor
    novo_valor = 0 if disponivel_atual == 1 else 1

    # Atualizar no banco
    cursor.execute('UPDATE Livros SET disponivel = ? WHERE id = ?', (novo_valor, id_livro))
    conexao.commit()

    print("Disponibilidade atualizada com sucesso!")
else:
    print("Livro não encontrado!")
