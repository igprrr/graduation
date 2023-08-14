'''-----------------------------------------------------------------------------------------------------------
#Crie, utilizando o widget Label e o método de posicionamento pack e seus argumentos, a seguinte interface:
-----------------------------------------------------------------------------------------------------------'''

import tkinter as tk

class Tela:
    def __init__(self, master):
        self.tela = master
        self.lbl = tk.Label(self.tela, text = 'topo', font = ('Arial', 12))
        self.lbl.pack()

        self.lbl2 = tk.Label(self. tela, text = 'rodapé', font = ('Arial', 12))
        self.lbl2.pack(side = tk.BOTTOM)

        self.lbl3 = tk.Label(self.tela, text = 'esquerda', font = ('Arial', 12))
        self.lbl3.pack(side = tk.LEFT, padx = 0, pady = 50)

        self.lbl4 = tk.Label(self.tela, text = 'direita', font = ('Arial', 12))
        self.lbl4.pack(side = tk.RIGHT, padx = 0, pady= 50)

janelaPrincipal = tk.Tk()
Tela(janelaPrincipal)
janelaPrincipal.mainloop()