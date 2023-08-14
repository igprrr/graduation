import tkinter as tk
import bd
from tkinter import messagebox


class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x200')
        self.frame = tk.Frame(self.janela)
        self.frame.pack()

        self.lbl_nome = tk.Label(self.janela, text='nome:')
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(self.janela, width=40)
        self.ent_nome.pack()

        self.lbl_email = tk.Label(self.janela, text='email:')
        self.lbl_email.pack()
        self.ent_email = tk.Entry(self.janela, width=40)
        self.ent_email.pack()

        self.lbl_tel = tk.Label(self.janela, text='telefone:')
        self.lbl_tel.pack()
        self.ent_tel = tk.Entry(self.janela, width=40)
        self.ent_tel.pack()

        self.btn_gravar = tk.Button(self.janela, text='gravar dados', command=self.gravar_dados)
        self.btn_gravar.pack()

    def gravar_dados(self):
        var_nome = self.ent_nome.get()
        var_email = self.ent_email.get()
        var_tel = self.ent_tel.get()
        if var_nome != '' and var_email != '' and var_tel != '':
            query = "insert into pessoas (nome, email, telefone) values ('"+var_nome+"', '"+var_email+"', '"+var_tel+"')"
            bd.manipula(query)
            messagebox.showinfo('Mensagem', 'informações realizada com sucesso')
            self.ent_nome.delete(0, tk.END)
            self.ent_email.delete(0, tk.END)
            self.ent_tel.delete(0, tk.END)
        else:
            messagebox.showerror('Alerta', 'Nome, Email e Telefone precisam ser preenchidos')

raiz = tk.Tk()
Tela(raiz)
raiz.mainloop()