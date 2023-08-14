#este codigo funciona como manipulaçao de inserir, apagar e mostrar tods que ja estão salvos em um banco de dados
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import bd

#função inicial
def principal():
    tv.delete(*tv.get_children())
    vquery = 'select * from produtos_informatica order by id_produtos'
    linhas = bd.dql(vquery)
    for i in linhas:
        tv.insert('', 'end', values = i)

#função de inserir
def inserir():
    if vteclados.get() == "" or vmouses.get() == "" or vmonitores.get() == "" or vplacas_de_video.get() == "" or vprocessadores.get() == "" or vgabinetes.get() == "" or vplacas_mae.get() == "":
        messagebox.showinfo(title = 'ERRO', message = 'Digite todos os dados')
        return
    try:
        vquery = "insert into produtos_informatica (teclados, mouses, monitores, placas_de_video, processadores, gabinetes, placas_mae) values ('"+vteclados.get()+"','"+vmouses.get()+"','"+vmonitores.get()+"','"+vplacas_de_video.get()+"','"+vprocessadores.get()+"','"+vgabinetes.get()+"','"+vplacas_mae.get()+"')"
        bd.dml(vquery)
    except:
        messagebox.showinfo(title = 'ERRO', message = 'Erro ao inserir')
        return
    principal()
    vteclados.delete(0, END)
    vmouses.delete(0, END)
    vmonitores.delete(0, END)
    vplacas_de_video.delete(0, END)
    vprocessadores.delete(0, END)
    vgabinetes.delete(0, END)
    vplacas_mae.delete(0, END)
    vteclados.focus()

#função de apagar
def apagar():
    vid = -1
    itemSelecionado = tv.selection()[0]
    valores = tv.item(itemSelecionado, 'values')
    vid = valores[0]
    try:
        vquery = 'delete from produtos_informatica where id_produtos =' +vid
        bd.dml(vquery)
    except:
        messagebox.showinfo(title = 'ERRO', message = 'Erro ao apagar')
        return
    tv.delete(itemSelecionado)

#função de pesquisa
def pesquisar():
    tv.delete(*tv.get_children())
    vquery = "select * from produtos_informatica where id_produtos like '%" +vid_produtospesquisar.get()+"%'"
    linhas = bd.dql(vquery)
    for i in linhas:
        tv.insert('','end', values = i)
app = Tk()
app.title('Dados')
app.geometry('1000x350')

#comandos do quadro 'informaçõs' do treeview
quadroGrid = LabelFrame(app, text = 'Informações')
quadroGrid.pack(fill = 'both', expand = 'yes', padx = 10, pady = 10)

tv = ttk.Treeview(quadroGrid, columns = ('id_produtos', 'teclados', 'mouses', 'monitores', 'placas_de_video', 'processadores', 'gabinetes', 'placas_mae'), show = 'headings')
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
tv.pack()
principal()

#comandos do quadro 'inserir' do treeview
quadroInserir = LabelFrame(app, text = 'Inserir novos dados')
quadroInserir.pack(fill = 'both', expand = 'yes', padx = 10, pady = 10)

lbteclados = Label(quadroInserir, text = 'TECLADOS')
lbteclados.pack(side = 'left')
vteclados = Entry(quadroInserir)
vteclados.pack(side = 'left', padx = 10)

lbmouses = Label(quadroInserir, text = 'MOU')
lbmouses.pack(side = 'left')
vmouses = Entry(quadroInserir)
vmouses.pack(side = 'left', padx = 10)

lbmonitores = Label(quadroInserir, text = 'MONIT')
lbmonitores.pack(side = 'left')
vmonitores = Entry(quadroInserir)
vmonitores.pack(side = 'left', padx = 0)

lbplacas_de_video = Label(quadroInserir, text = 'GPU')
lbplacas_de_video.pack(side = 'left')
vplacas_de_video = Entry(quadroInserir)
vplacas_de_video.pack(side = 'left', padx = 10)

lbprocessadores = Label(quadroInserir, text = 'CPU')
lbprocessadores.pack(side = 'left')
vprocessadores = Entry(quadroInserir)
vprocessadores.pack(side = 'left', padx = 10)

lbgabinetes = Label(quadroInserir, text = 'GAB')
lbgabinetes.pack(side = 'left')
vgabinetes = Entry(quadroInserir)
vgabinetes.pack(side = 'left', padx = 10)

lbplacas_mae = Label(quadroInserir, text = 'PM')
lbplacas_mae.pack(side = 'left')
vplacas_mae = Entry(quadroInserir)
vplacas_mae.pack(side = 'left', padx = 10)
btn_inserir = Button(quadroInserir, text = 'Inserir dados', command = inserir)
btn_inserir.pack(side = 'left', padx = 10)

#comandos do quadro 'Dados'
quadroPesquisar = LabelFrame(app, text = 'Dados')
quadroPesquisar.pack(fill = 'both', expand = 'yes', padx = 0, pady = 10)

lbid_produtos = Label(quadroPesquisar, text = 'ID')
lbid_produtos.pack(side = 'left')
vid_produtospesquisar = Entry(quadroPesquisar)
vid_produtospesquisar.pack(side = 'left', padx = 10)
btn_pesquisar = Button(quadroPesquisar, text = 'Pesquisar', command = pesquisar)
btn_pesquisar.pack(side = 'left', padx = 10)
btn_todos = Button(quadroPesquisar, text = 'Mostrar todos', command = principal)
btn_todos.pack(side = 'left', padx = 10)
btn_apagar = Button(quadroPesquisar, text = 'Apagar', command = apagar )
btn_apagar.pack(side = 'left', padx = 0, pady = 10)

app.mainloop()