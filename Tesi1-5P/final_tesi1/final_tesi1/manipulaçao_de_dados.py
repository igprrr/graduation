#este código funciona como manipulação de inserir, apagar e obter informações de dados inseridos no treeview(sem esta em um banco de dados)
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#funçao de inserir
def inserir():
    if vid_produtos.get() == "" or vteclados.get() == "" or vmouses.get() == '' or vmonitores.get() == '' or vplacas_de_video.get() == '' or vprocessadores.get() == '' or vgabinetes.get() == '' or vplacas_mae.get() == '':
        messagebox.showinfo(title = 'ERRO', message = 'Digite todos os dados')
        return
    tv.insert('', 'end', values = (vid_produtos.get(), vteclados.get(), vmouses.get(), vmonitores.get(), vplacas_de_video.get(), vprocessadores.get(), vgabinetes.get(), vplacas_mae.get()))
    vid_produtos.delete(0, END)
    vteclados.delete(0, END)
    vmouses.delete(0, END)
    vmonitores.delete(0, END)
    vplacas_de_video.delete(0, END)
    vprocessadores.delete(0, END)
    vgabinetes.delete(0, END)
    vplacas_mae.delete(0, END)
    vid_produtos.focus()

#fnçao de deletar
def deletar():
    try:
        itemSelecionado = tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title = 'ERRO', message = 'Selecione um objeto a ser apagado')
def obter():
    try:
        itemSelecionado = tv.selection()[0]
        valores = tv.item(itemSelecionado, 'values')
        print('ID...............: '+ valores[0])
        print('TECLADOS.........: '+ valores[1])
        print('MOUSES...........: '+ valores[2])
        print('MONITORES........: '+ valores[3])
        print('PLACAS DE VIDEO..: '+ valores[4])
        print('PROCESSADORES....: '+ valores[5])
        print('GABINETES........: '+ valores[6])
        print('PLACAS MAE.......: '+ valores[7])
    except:
        messagebox.showinfo(title = 'ERRO', message = 'Selecione um objeto a ser mostrado')

app = Tk()
app.title('Informaçoes')
app.geometry('1000x350')

lbid_produtos = Label(app, text = 'ID')
vid_produtos = Entry(app)

lbteclados = Label(app, text = 'TECLADOS')
vteclados = Entry(app)

lbmouses = Label(app, text = 'MOUSES')
vmouses = Entry(app)

lbmonitores = Label(app, text = 'MONITORES')
vmonitores = Entry(app)

lbplacas_de_video = Label(app, text = 'PLACAS DE VIDEOS')
vplacas_de_video = Entry(app)

lbprocessadores = Label(app, text = 'PROCESSADORES')
vprocessadores = Entry(app)

lbgabinetes = Label(app, text = 'GABINETES')
vgabinetes = Entry(app)

lbplacas_mae = Label(app, text = 'PLACAS MÃES')
vplacas_mae = Entry(app)

#codigos da caixa do treeview(com os dados)
tv = ttk.Treeview(app, columns = ('id_produtos', 'teclados', 'mouses', 'monitores', 'placas_de_video', 'processadores', 'gabinetes', 'placas_mae'), show = 'headings')
tv.column('id_produtos', minwidth = 0, width = 30)
tv.column('teclados', minwidth = 0, width = 100)
tv.column('mouses', minwidth = 0, width = 100)
tv.column('monitores', minwidth = 0, width = 100)
tv.column('placas_de_video', minwidth = 0, width = 160)
tv.column('processadores', minwidth = 0, width = 100)
tv.column('gabinetes', minwidth = 0, width = 100)
tv.column('placas_mae', minwidth = 0, width = 100)

tv.heading('id_produtos', text = 'ID')
tv.heading('teclados', text = 'TECLADOS')
tv.heading('mouses', text = 'MOUSES')
tv.heading('monitores', text = 'MONITORES')
tv.heading('placas_de_video', text = 'PLACAS DE VIDEO')
tv.heading('processadores', text = 'PROCESSADORES')
tv.heading('gabinetes', text = 'GABINETES')
tv.heading('placas_mae', text = 'PLACAS MAE')

#botoes
btn_inserir = Button(app, text = 'Inserir', command = inserir)
btn_deletar = Button(app, text = 'Deletar', command = deletar)
btn_obter = Button(app, text = 'Obter', command = obter)

lbid_produtos.grid(column = 0, row = 0)
vid_produtos.grid(column = 0, row = 1)

lbteclados.grid(column = 1, row = 0, stick = 'w')
vteclados.grid(column = 1, row = 1)

lbmouses.grid(column = 2, row = 0, stick = 'w')
vmouses.grid(column = 2, row = 1)

lbmonitores.grid(column = 3, row = 0, stick = 'w')
vmonitores.grid(column = 3, row = 1)

lbplacas_de_video.grid(column = 4, row = 0, stick = 'w')
vplacas_de_video.grid(column = 4, row = 1)

lbprocessadores.grid(column = 5, row = 0, stick = 'w')
vprocessadores.grid(column = 5, row = 1)

lbgabinetes.grid(column = 6, row = 0, stick = 'w')
vgabinetes.grid(column = 6, row = 1)

lbplacas_mae.grid(column = 7, row = 0, stick = 'w')
vplacas_mae.grid(column = 7, row = 1)

tv.grid(column = 0, row = 8, columnspan = 8, pady = 10)

btn_inserir.grid(column = 2, row = 9)
btn_deletar.grid(column = 3, row = 9)
btn_obter.grid(column = 4, row = 9)

app.mainloop()