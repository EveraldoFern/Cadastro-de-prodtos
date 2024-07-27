import sqlite3 as lite


# Criando conexão
con = lite.connect('defeitos.db')


# Inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Produtos (codigo , oem , descricao , montadora, material , peso  , diametro_garg , diametro_bico_me , diametro_bico_ma ,imagem ) VALUES (?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Inserir dados
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Produtos SET codigo=?, oem=?, descricao=?, montadora=?, material=?,  peso=?, diametro_garg=?, diametro_bico_me=?, diametro_bico_ma=? ,imagem=? WHERE id=?"
        cur.execute(query, i)


# Deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Produtos WHERE id=? "
        cur.execute(query, i)


# Ver dados
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT* FROM Produtos "
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


# Ver dados
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT* FROM Produtos WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual


def pesquisar_cadastro(codigo):
    con = lite.connect('dados.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Produtos WHERE codigo =?', (codigo,))
        resultado = cur.fetchone()

        return resultado


