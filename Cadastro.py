# importando o SQLite
import sqlite3 as lite


# Criando conexão
con = lite.connect('dados.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Produtos(id INTEGER PRIMARY KEY AUTOINCREMENT,codigo TEXT, oem TEXT, descricao TEXT, montadora TEXT, material TEXT, peso TEXT , diametro_garg TEXT, diametro_bico_me TEXT, diametro_bico_ma TEXT,imagem TEXT)")

