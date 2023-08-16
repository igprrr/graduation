'''Exercício 1
*Crie uma interface gráfica para escrever em um arquivo

*A interface deve apresentar widgets, tais como: Entry, Checkbuton, Radiobutton, etc para preencher informações

*Utilize um arquivo com a extensão .txt para armazenar as informações capturadas na interface gráfica'''

import tkinter as tk
from tkinter import filedialog

class Tela:
    def __init__(self, master):

        self.nossaTela = master
        self.barraMenu = tk.Menu(self.nossaTela)
        self.arquivoAberto = None
        self.criaArq()
        self.barraMenu.add_command(label = 'Ler arquivo', command = self.lerArquivo)
        self.barraMenu = tk.Menu(self.nossaTela)
        self.nossaTela.config(menu = self.barraMenu)
        # comando que ler arquivo.
        self.barraMenu.add_command(label = 'Ler arquivo', command = self.lerArquivo)

    #método que possibilita criar o arquivo txt
    def criaArq(self):
        #entrada de dados
        self.lbl1 = tk.Label(self.nossaTela, text = 'Digite seu nome:', font = ('Arial',12))
        self.entradaNome = tk.Entry(self.nossaTela, font = ('Arial',12))
        self.lbl1.grid(column = 0)
        self.entradaNome.grid(row = 0, column = 1, padx = 20)

        self.lbl2 = tk.Label(self.nossaTela, text = 'Digite seu telefone:', font = ('Arial',12))
        self.entradaTel = tk.Entry(self.nossaTela,font = ('Arial', 12))
        self.lbl2.grid(row = 1, column = 0)
        self.entradaTel.grid(row = 1, column = 1, padx = 20)

        self.lbl3 = tk.Label(self.nossaTela, text = 'Digite seu email:', font = ('Arial', 12))
        self.entradaEmail = tk.Entry(self.nossaTela, font = ('Arial', 12))
        self.lbl3.grid(row = 2, column = 0)
        self.entradaEmail.grid(row = 2, column = 1, padx = 20)

        self.cadastra = tk.Button(self.nossaTela, text = 'Salvar', command = self.salvar)
        self.cadastra.grid(row = 3,column = 0,columnspan = 2,pady = 20)

    #método que salva os dados
    def salvar(self):
        
        nome = self.entradaNome.get()
        telefone = self.entradaTel.get()
        email = self.entradaEmail.get()

        if self.arquivoAberto is None:
            self.arquivoAberto = filedialog.asksaveasfilename(defaultextension = '.txt', filetypes = (('Arquivos de Texto','*.txt'),('Todos arquivos','*.*') ))
        if self.arquivoAberto is not None:
            dados = open(self.arquivoAberto,'a')

            #dados que aparecem no console do arquivo salvo.
            dados.write('\nNome:{}\nTelefone:{}\nEmail:{}'.format(nome, telefone, email))

        else:
            print("Erro")

    #leitura dos arquivos
    def lerArquivo(self):
        caminho = filedialog.askopenfile(mode = 'r', initialdir = '/Downloads', title = 'Selecione um arquivo', filetypes = (('Arquivos de texto', '*.txt'), ('Arquivos Python', '*.py')))
        #se realmente foi escolhido um arquivo para ser aberto.
        if caminho:
            #O conteúdo é lido de toda a extensão do arquivo
            conteudo = caminho.read()
            #Em seguida printado.
            print(conteudo)
        else:
            print('Por favor escolha um arquivo')

janelaprincipal = tk.Tk()
Tela(janelaprincipal)
janelaprincipal.mainloop()