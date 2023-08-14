#código do banco de dados para as devidas manipulações
import sqlite3
from sqlite3 import Error

caminho = 'C:\\Users\\igorr\\Desktop\\final_tesi1\\final_tesi1.db'
def conexao():
    vcon = None
    try:
        vcon = sqlite3.connect(caminho)
        print('conexao foi realizada')
    except Error as ex:
        print('erro de conexao')
    return vcon

def dql(query): #select
    vcon = conexao()
    c = vcon.cursor()
    c.execute(query)
    res = c.fetchall()
    vcon.close()
    return res

def dml(query):
    try:
        vcon = conexao()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)