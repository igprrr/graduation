import sqlite3
from sqlite3 import Error

caminho = 'C:\\Users\\igorr\\Desktop\\atv_complementar_n2\\exercicio_2.db'

def conexao():
    con = None
    try:
        con = sqlite3.connect(caminho)
        print("Conexao foi realizada")
    except Error as er:
        print("Erro na conexao")
    return con

def consulta(query):    #select
    con = conexao()
    cursor = con.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    con.close()
    return resultado

def manipula(query): #insert, update e delete
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        con.close()
        #print("Operação relizada com sucesso")
    except Error as er:
        print(er)

def deletar(c, s):
    try:
        cursor = c.cursor()
        cursor.execute(s)
        c.commit()
        print("Registro foi removido com sucesso!")
    except Error as ex:
        print(ex)