import bd
import tkinter as tk
from tkinter import ttk

class TelaSecundaria():
    def __init__(self, master, origem):
        self.janela_secundaria = master
        self.principal = origem

        self.lbl_nome = tk.Label(self.janela_secundaria, text="Nome:")
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(self.janela_secundaria, width=150, textvariable = self.v_nome)
        self.ent_nome.pack()

        self.lbl_telefone = tk.Label(self.janela_secundaria, text = 'Telefone:')
        self.lbl_telefone.pack()
        self.ent_telefone = tk.Entry(self.janela_secundaria, widht = 150, textvariable = self.v_telefone)
        self.ent_telefone.pack()

        self.lbl_email = tk.Label(self.janela_secundaria, text="Email:")
        self.lbl_email.pack()
        self.ent_email = tk.Entry(self.janela_secundaria, width=150, textvariable=self.v_email)
        self.ent_email.pack()


class Tela():

    def __init__(self, master):
        self.janela = master
        self.janela.geometry("500x620")
        self.janela.title('Dados')
        self.frame = tk.Frame(self.janela)
        self.frame.pack()

        self.lbl_nome = tk.Label(self.frame, text= 'Nome:')
        self.lbl_nome.pack(padx = 50)
        self.ent_nome = tk.Entry(self.frame, width=100)
        self.ent_nome.pack(padx = 10)

        self.lbl_telefone = tk.Label(self.frame, text='Telefone:')
        self.lbl_telefone.pack()
        self.ent_telefone = tk.Entry(self.frame, width=80)
        self.ent_telefone.pack()

        self.lbl_email = tk.Label(self.frame, text = 'Email')
        self.lbl_email.pack()
        self.ent_email = tk.Entry(self.frame, width = 80)
        self.ent_email.pack()
        
        #componente de Grid
        
        self.trv = ttk.Treeview(self.frame, columns=('id', 'nome', 'telefone', 'email'), show='headings')
        self.trv.column('id', minwidth = 0, width=30)
        self.trv.heading('id', text='ID_PESSOA')
        self.trv.column('nome', minwidth = 0,  width=120)
        self.trv.heading('nome', text='NOME')
        self.trv.column('telefone', minwidth = 0, width = 120)
        self.trv.heading('telefone', text = 'EMAIL')
        self.trv.column('email', minwidth = 0, width=130)
        self.trv.heading('email', text='TELEFONE')

        #chamar a função atualiza(nao completada)
        self.atualiza_grid()
        self.trv.pack(pady= 10)

        #botoes
        self.btn_gravar = tk.Button(self.frame, text='Adicionar', command=self.adicionar_dados)
        self.btn_gravar.pack(side = 'left', padx = 10)

        self.btn_atualizar = tk.Button(self.frame, text='Atualiza', command=self.atualizar_dados)
        self.btn_atualizar.pack(side = 'left', pady = 14)

        self.btn_remover = tk.Button(self.frame, text='Remover', command=self.remover_dados)
        self.btn_remover.pack(side = 'left', pady = 16)

        #ainda nao funfando
    def atualizar_dados(self):
        self.atualiza_grid()
        self.ent_nome.delete(0, tk.END)

    def remover_dados(self):
        indice_selecionado = self.trv.selection()[0]
        id_pessoa = self.trv.item(indice_selecionado, 'values')[0]
        self.trv.delete(indice_selecionado)
        query = "DELETE FROM pessoas WHERE id_pessoa ='"+id_pessoa+"'"
        bd.manipula(query)
        self.atualiza_grid()
        
    #nao fufando
    def atualiza_grid(self):
        self.trv.delete(*self.trv.get_children())
        # inserindo elementos dentro do grid a partir do banco de dados
        query = "SELECT * FROM pessoas"
        lista = bd.consulta(query)
        for i in lista:
            self.trv.insert("", "end", values=i)

    def adicionar_dados(self):
        nome = self.ent_nome.get()
        telefone = self.ent_telefone.get()
        email = self.ent_email.get()
        query = "INSERT INTO pessoas (nome, telefone, email) VALUES ('"+nome+"','"+telefone+"','"+email+"');"
        bd.manipula(query)
        self.atualiza_grid()
        self.ent_nome.delete(0, tk.END)
        self.ent_telefone.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)

raiz = tk.Tk()
Tela(raiz)
raiz.mainloop()