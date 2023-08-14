'''---------------------------------------------------
#Crie a seguinte interface usando o gerenciador grid.
---------------------------------------------------'''

import tkinter as tk

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        self.lbl = tk.Frame(self.nossaTela)
        self.lbl.pack()

        self.lbl2 = tk.Frame(self.nossaTela)
        self.lbl2.pack()

        self.lbl3 = tk.Frame(self.nossaTela)
        self.lbl3.pack()
        
        self.botao = tk.Button(self.lbl, text='1', width = 2, height = 2)
        self.botao.pack()

        self.botao2 = tk.Button(self.lbl2, text='2', width =2, height = 2)
        self.botao2.pack(side = tk.LEFT)

        self.botao3 = tk.Button(self.lbl2, text='3', width = 2, height = 2)
        self.botao3.pack(side = tk.LEFT)

        self.botao4 = tk.Button(self.lbl3, text='4', width = 2, height = 2)
        self.botao4.pack(side = tk.LEFT)

        self.botao5 = tk.Button(self.lbl3, text='5', width = 2, height = 2)
        self.botao5.pack(side = tk.LEFT)

        self.botao6 = tk.Button(self.lbl3, text="6", width = 2, height = 2)
        self.botao6.pack(side = tk.LEFT)

telaprincipal = tk.Tk()
Tela(telaprincipal)
telaprincipal.mainloop()