'''-------------------------------------------------------------------------------------------------------------
#Crie a interface gráfica com o gerenciador de layout place e o uma funcionalidade para somar dois números reais
-------------------------------------------------------------------------------------------------------------'''

import tkinter as tk
from tkinter.constants import LEFT

class Tela: 
    def __init__(self, master):
 
        self.n1 = tk.Frame(master)
        self.n1.pack()                
  
        self.n2 = tk.Frame(master)
        self.n2.pack()
        
        self.Tela = tk.Frame(master, pady = 8)
        self.Tela.pack()
      
        self.result = tk.Frame(master)
        self.result.pack()

        self.botao = tk.Frame(master, pady = 8)
        self.botao.pack()

        somar = tk.Button(self.Tela, text = 'SOMAR',command = self.somar)
        somar.pack(side = LEFT)                  
        
        tk.Label(self.n1, text = 'Valor1 :', width = 8).pack(side = LEFT)
        self.valor1 = tk.Entry(self.n1, width = 4)
        self.valor1.pack(side = LEFT)

        tk.Label(self.n2, text = 'Valor2 :', width = 8).pack(side = LEFT)
        self.valor2 = tk.Entry(self.n2, width = 4)
        self.valor2.pack(side = LEFT)

        self.valor_result = tk.Label(self.result, width = 12)
        self.valor_result.pack(side = LEFT)

    def somar(self):
        valor1 = self.valor1.get()
        valor2 = self.valor2.get()
        valor1 = float(valor1)
        valor2 = float(valor2)
        somado = valor1 + valor2
        somado = float(somado)
        self.valor_result['text'] = '%.1f' %(somado)            
    
principal = tk.Tk()
Tela(principal)
principal.mainloop()