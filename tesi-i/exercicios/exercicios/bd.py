#parte de conexao com o banco de dados

import sqlite3
from sqlite3 import Error

caminho = 'C:\\Users\\igorr\\Desktop\\ex1\\exercicio_1.db'
def conexao():
    con = None
    try:
        con = sqlite3.connect(caminho)
        print('conexao foi realizada')
    except Error as er:
        print('erro de conexao')
    return con

def consulta(query):
    con = conexao()
    cursor = con.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    con.close()
    return resultado

def manipula(query):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        con.close()
        #print('operaçao realizada')
    except Error as er:
        print(er)

def apagar(c, s):
    try:
        cursor = c.cursor()
        cursor.execute(s)
        c.commit()
        print("Registro foi removido com sucesso!")
    except Error as ex:
        print(ex)

