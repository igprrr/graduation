'''Crie uma interface gráfica para abrir(ler) um arquivo
● O usuário pode escolher o tipo do arquivo
● Utilize 3 tipos de arquivo:
– .txt
– .png
– .jpg
● O conteúdo do arquivo deve ser apresentado na interface gráfica'''

import tkinter as tk
from tkinter import filedialog
import os #módulo usado para usar as funçoes do SO dos sistemas de arquivos

janela = tk.Tk()
caixa = []

def arquivos():
    arquivo = filedialog.askopenfile(filetypes = (('*',''), ('.txt, .jpg, ,png', '*.*')))
    caixa.append(arquivo)
    print(arquivo)

def exe_arquivos():
    for caixas in caixa:
        os.startfile(caixas.name) #do módulo, retorna assim que a aplicação associada é iniciada

tela = tk.Label(janela, height = 5, width = 20)
tela.pack()

#abre a caixa de seleçao de arquivo .txt, .png ou .jpg
botaoAbrir = tk.Button(janela, text = "Abrir arquivo", padx = 10, pady = 5, command = arquivos)
botaoAbrir.pack()

#apos ter clicado no arquivo desejado, ele é apresentado no terminal e esse botao o carrega
botaoExe = tk.Button(janela, text = "Executar arquivo", padx = 10, pady = 5, command = exe_arquivos)
botaoExe.pack()

janela.mainloop()