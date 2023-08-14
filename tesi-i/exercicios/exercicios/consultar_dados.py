'''
exercicio 1
* Crie uma interface gráfica para consultar um registro em uma tabela no banco de dados
* A interface deve apresentar um campo de entrada para informar uma característica (coluna) da tabela
* Em caso de sucesso, mostre o registro em uma caixa de mensagem, caso contrário mostra uma mensagem de alerta
'''

import tkinter as tk
import bd
from tkinter import messagebox

class SegundaTela():
    def __init__(self, master, origem, resposta):
        self.segunda_janela = master
        self.original = origem
        self.segunda_janela.title('Atualizar pessoa')

        self.v_nome = tk.StringVar(self.segunda_janela, resposta[0][0])
        self.v_email = tk.StringVar(self.segunda_janela, resposta[0][1])
        self.v_tel = tk.StringVar(self.segunda_janela, resposta[0][2])
        
        self.lbl_nome = tk.Label(self.segunda_janela, text = 'nome:')
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(self.segunda_janela, width = 40, textvariable = self.v_nome)
        self.ent_nome.pack()

        self.lbl_email = tk.Label(self.segunda_janela, text = 'email:')
        self.lbl_email.pack()
        self.ent_email = tk.Entry(self.segunda_janela, width = 40, textvariable = self.v_email)
        self.ent_email.pack()

        self.lbl_tel = tk.Label(self.segunda_janela, text = 'telefone:')
        self.lbl_tel.pack()
        self.ent_tel = tk.Entry(self.segunda_janela, width = 40, textvariable = self.v_tel)
        self.ent_tel.pack()

        self.botao_voltar = tk.Button(self.segunda_janela, text = 'Voltar', command = self.voltar)
        self.botao_voltar.pack()

        self.botao_gravar = tk.Button(self.segunda_janela, text = 'atualizar dados', command = self.atualizar_dados)
        self.botao_gravar.pack()

        self.botao_apagar = tk.Button(self.segunda_janela, text = 'Apagar', command = self.apagar)
        self.botao_apagar.pack()

    def voltar(self):
        self.original.deiconify()
        self.segunda_janela.destroy()

class Tela():
    def __init__(self, master):
        self.janela = master
        self.janela.title('interface de pessoas')

        self.lbl_nome = tk.Label(self.janela, text = 'Nome: ')
        self.lbl_nome.pack()
        self.ent_nome = tk.Entry(self.janela, width = 50)
        self.ent_nome.pack()
        self.botao_consultar = tk.Button(self.janela, text = 'Pesquisar', command = self.consultar_dados)
        self.botao_consultar.pack()

    def consultar_dados(self):
        var_nome = self.ent_nome.get()
        query = "select nome, email, telefone from pessoas where nome LIKE '%" + var_nome + "%' ;"
        resposta = bd.consulta(query)
        print(resposta)
        mostrar = ''
        for r in resposta:
            mostrar += r[0] + '\n'
        if resposta == []:
            messagebox.showerror('Aviso','Nenhum registro encontrado')
        else:
            self.nova_janela = tk.Toplevel(self.janela)
            SegundaTela(self.nova_janela, self.janela, resposta)
            self.janela.iconify()
        self.ent_nome.delete(0, tk.END)

raiz = tk.Tk()
Tela(raiz)
raiz.mainloop()