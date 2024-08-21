import sqlite3 as SQL 

def corresp_exata(palavra: str) -> list:
    """

    Este método irá:
    1. Aceitar uma string
    2. Buscar ela no dicionário por uma correspondência exta
    3. Se sucesso, retorna a definição
    4. Se não, retorna lista vazia
    """
    #Estabelecer uma conexão com a base de dados dicionário
    db = SQL.connect("data/Dictionary.db")
    #Procurar por correspondências exatas
    sql_query = "SELECT word, defn from words WHERE word=?"
    #Executa a consulta SQL definida anteriormente, substituindo "?" pelo
    #valor da variável "palavra"
    #fetchall RECUPERA todos os resultados da consulta
    correspondencia = db.execute(sql_query, (palavra, )).fetchall()
    #fechar a conexão com a base de dados
    db.close()
    return correspondencia

def corresp_aproximada(palavra: str) -> list:

    #Estabelecer uma conexão com a base de dados dicionário
    db = SQL.connect("data/Dictionary.db")
    #Procurar por correspondências aproximada
    sql_query = "SELECT word, defn from words WHERE word LIKE ?"
    #Executa a consulta SQL definida anteriormente, substituindo "?" pelo
    #valor da variável "palavra"
    #fetchall RECUPERA todos os resultados da consulta
    correspondencia = db.execute(sql_query, ("%" + palavra, + "%",)).fetchall()
    #fechar a conexão com a base de dados
    db.close()
    return correspondencia