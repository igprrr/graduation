import tkinter as tk
import bd
from tkinter import messagebox

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title("Remover Dados")

        self.lbl_nome = tk.Label(self.janela, text='Nome: ')
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(self.janela, width = 40)
        self.ent_nome.pack()
        self.btn_remover = tk.Button(self.janela, text='Apagar',
                                       command=self.remover_dados)
        self.btn_remover.pack()

    conexao1 = bd.conexao()

    def remover_dados(self):
        var_nome = self.ent_nome.get()
        query = "select nome, email from pessoas where nome = '" + var_nome + "' ;"
        resposta = bd.consulta(query)
        sql_delete = "delete from pessoas where nome= '"+var_nome+"'"
        bd.apagar(bd.conexao(), sql_delete)

        if resposta == []:
            messagebox.showerror('Resgistro não encontrado')
        else:
            messagebox.showinfo("Cadastro '" + resposta [0][0] + "' foi removido")

raiz = tk.Tk()
Tela(raiz)
raiz.mainloop()