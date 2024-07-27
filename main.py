import os
from tkinter import*
from tkinter import Tk, StringVar, ttk
import ImageTk
from tkinter import messagebox, filedialog as fd
from PIL import Image, ImageTk

from view import*


################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

################# criando janela ###############

janela = Tk()
janela.title("")
janela.geometry('1160x900')
janela.configure(background=co9)
janela.resizable(width=True, height=True)

style = ttk.Style(janela)
style.theme_use("clam")

################# Frames ####################

frameCima = Frame(janela, width=11000, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1100, height=320, bg=co1, pady=20, relief="flat")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1100, height=500, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=1, padx=1, sticky=NSEW)

global tree
#Criando funções
def inserir():
    global imagem, imagem_string, l_imagem

    codigo = e_codigo.get()
    oem = e_oem.get()
    descricao = e_descricao.get()
    montadora = e_montadora.get()
    material = e_material.get()
    peso = e_peso.get()
    diametro_garg = e_diametro_garg.get()
    diametro_bico_ma = e_diametro_bico_ma.get()
    diametro_bico_me = e_diametro_bico_me.get()
    imagem = imagem_string

    lista_inserir = [codigo, oem, descricao, montadora, material, peso, diametro_garg, diametro_bico_ma, diametro_bico_me, imagem]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_codigo.delete(0, 'end')
    e_oem.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_montadora.delete(0, 'end')
    e_material.delete(0, 'end')
    e_peso.delete(0, 'end')
    e_diametro_garg.delete(0, 'end')
    e_diametro_bico_ma.delete(0, 'end')
    e_diametro_bico_me.delete(0, 'end')


    mostrar()
##################################################################################################
def atualizar():
    global imagem, imagem_string, l_imagem

    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_codigo.delete(0, 'end')
        e_oem.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_montadora.delete(0, 'end')
        e_material.delete(0, 'end')
        e_peso.delete(0, 'end')
        e_diametro_garg.delete(0, 'end')
        e_diametro_bico_ma.delete(0, 'end')
        e_diametro_bico_me.delete(0, 'end')



        id = int(treev_lista[0])
        e_codigo.insert(0, treev_lista[1])
        e_oem.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_montadora.insert(0, treev_lista[4])
        e_material.insert(0, treev_lista[5])
        e_peso.insert(0, treev_lista[6])
        e_diametro_garg.insert(0, treev_lista[7])
        e_diametro_bico_ma.insert(0, treev_lista[8])
        e_diametro_bico_me.insert(0, treev_lista[9])

        def update():
            global imagem,imagem_string, l_imagem

            codigo = e_codigo.get()
            oem = e_oem.get()
            descricao = e_descricao.get()
            montadora = e_montadora.get()
            material = e_material.get()
            peso = e_peso.get()
            diametro_garg = e_diametro_garg.get()
            diametro_bico_ma = e_diametro_bico_ma.get()
            diametro_bico_me = e_diametro_bico_me.get()

            imagem = imagem_string

            if imagem == '':
                imagem = e_peso.insert(0, treev_lista[10])

            lista_atualizar = [codigo, oem, descricao, montadora, material, peso, diametro_garg, diametro_bico_ma, diametro_bico_me, imagem, id]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')

                    return

            atualizar_dados(lista_atualizar)

            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_codigo.delete(0, 'end')
            e_oem.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_montadora.delete(0, 'end')
            e_material.delete(0, 'end')
            e_peso.delete(0, 'end')
            e_diametro_garg.delete(0, 'end')
            e_diametro_bico_ma.delete(0, 'end')
            e_diametro_bico_me.delete(0, 'end')

            botao_confirmar.destroy()

            mostrar()

        botao_confirmar = Button(frameMeio, command=update, text="Confirmar".upper(), width=13, height=1, bg=co2, fg=co1,font=('ivy 8 bold'),relief=RAISED, overrelief=RIDGE)
        botao_confirmar.place(x=330, y=185)


    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

###################################################################################################
def deletar():
    try:
        treev_dados =tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showerror('Sucesso', 'Os dados forma deletados com sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dodos da tabela')
##################################################################################################
def pesquisar():
    global imagem, imagem_string, l_imagem

    codigo = e_codigo.get()
    entries = [e_codigo, e_oem, e_descricao, e_montadora, e_material, e_peso, e_diametro_garg, e_diametro_bico_ma, e_diametro_bico_me]

    try:
        # Tenta converter para inteiro se o código for apenas numérico
        codigo = int(codigo) if codigo.isdigit() else codigo
    except ValueError as e:
        print(f"Erro ao converter o código: {e}")
        return  # sai da função se houver erro

    dados = pesquisar_cadastro(codigo)

    imagem = None  # define imagem como None por padrão

    if dados:  # verifica se os dados foram encontrados
        # Limpa os campos de entrada
        for entry in [e_codigo, e_oem, e_descricao, e_montadora, e_material, e_peso, e_diametro_garg, e_diametro_bico_ma, e_diametro_bico_me]:
            entry.delete(0, 'end')
            index = entries.index(entry)  # Obtém o índice do widget na lista
            entry.insert(END, dados[index + 1])  # Usa o índice para acessar dados

        imagem_string = dados[10]  # Supondo que dados[10] é o caminho da imagem

        if imagem_string and os.path.exists(imagem_string):
            imagem = Image.open(imagem_string)
            imagem = imagem.resize((240, 240))
            imagem = ImageTk.PhotoImage(imagem)

            # Cria ou atualiza o label da imagem
            if 'l_imagem' in globals():
                l_imagem.configure(image=imagem)
                l_imagem.image = imagem  # Mantém uma referência
            else:
                l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
                l_imagem.place(x=620, y=25)
        else:
            print("Imagem não encontrada ou arquivo não existe")
    else:
        print("Código não encontrado")
    if dados:  # verifica se os dados foram encontrados

# Limpa os campos de entrada e insere os dados
        for i, entry in enumerate(entries):
            entry.delete(0, 'end')
            entry.insert(END, dados[i+1])  # Ajuste o índice conforme necessário

##################################################################################################       
#Botão para escolher imagem
global imagem, imagem_string, l_imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # Abrindo imagem na janela
    
    imagem = Image.open(imagem)
    imagem = imagem.resize((250, 250))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=550, y=15)


#Função para ver imagem/item
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    iten = ver_item(valor)

    imagem = iten[0][10]

    # Abrindo imagem - ver item
    imagem = Image.open(imagem)
    imagem = imagem.resize((240, 240))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=620, y=25)

l_Produto_imagem = Label(frameMeio, text='  Imagem do produto  ' ,width=35, height=15,anchor=CENTER, font=('Ivy 15 bold'), bg=co6, fg=co1, relief=FLAT)
l_Produto_imagem.place(x=550, y=23)

#########################################################################################

# Abrindo imagem
app_img = Image.open('Marvini.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text="    CADASTRO DE PRODUTOS MARVINI ", width=1150, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)


# criando entradas
l_codigo = Label(frameMeio, text="Código", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_codigo.place(x=10, y=10)

e_codigo = Entry(frameMeio, width=30, justify='left', relief="solid")
e_codigo.place(x=130, y=11)

l_oem = Label(frameMeio, text="OEM", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_oem.place(x=10, y=40)

e_oem = Entry(frameMeio, width=30, justify='left', relief="solid")
e_oem.place(x=130, y=41)


l_descricao = Label(frameMeio, text="Descrição", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=470, y=0)

e_descricao = Entry(frameMeio, width=70, justify='left', relief="solid")
e_descricao.place(x=550, y=0)

l_montadora = Label(frameMeio, text="Montadora", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_montadora.place(x=10, y=70)

e_montadora = Entry(frameMeio, width=30, justify='left', relief="solid")
e_montadora.place(x=130, y=70)

###############################################################################

l_peso = Label(frameMeio, text="Peso", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_peso.place(x=10, y=100)

e_peso = Entry(frameMeio, width=20, justify='left', relief="solid")
e_peso.place(x=130, y=101)

l_material = Label(frameMeio, text="Material", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_material.place(x=10, y=130)

e_material = Entry(frameMeio, width=20, justify='left', relief="solid")
e_material.place(x=130, y=131)

l_diametro_garg = Label(frameMeio, text="Diâmetro do gargalo", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_diametro_garg.place(x=10, y=160)

e_diametro_garg = Entry(frameMeio, width=20, justify='left', relief="solid")
e_diametro_garg.place(x=160, y=161)

l_diametro_bico_ma = Label(frameMeio, text="Diâm. do bico menor", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_diametro_bico_ma.place(x=10, y=190)

e_diametro_bico_ma = Entry(frameMeio, width=20, justify='left', relief="solid")
e_diametro_bico_ma.place(x=160, y=191)

l_diametro_bico_me = Label(frameMeio, text="Diâm. do bico maior", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_diametro_bico_me.place(x=10, y=220)

e_diametro_bico_me = Entry(frameMeio, width=20, justify='left', relief="solid")
e_diametro_bico_me.place(x=160, y=221)

#################################################################################################################################################
l_carregar = Label(frameMeio, text="Imagem do item", height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=250)

botao_carregar = Button(frameMeio, command=escolher_imagem, width=20, compound=CENTER, anchor=CENTER, text="carregar".upper(),  overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_carregar.place(x=160, y=251)

# Botao Inserir
img_add  = Image.open('add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(frameMeio, command=inserir, image=img_add, compound=LEFT, anchor=NW, text="   Adicionar".upper(), width=90, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_inserir.place(x=330, y=62)

# Botao Atualizar
img_update = Image.open('update.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

botao_atualizar = Button(frameMeio, command= atualizar, image=img_update, compound=LEFT, anchor=NW, text="   Atualizar".upper(), width=90, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_atualizar.place(x=330, y=160)


# Botao Deletar
img_delete  = Image.open('delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_deletar = Button(frameMeio, command= deletar, image=img_delete, compound=LEFT, anchor=NW, text="   Deletar".upper(), width=90, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_deletar.place(x=330, y=110)

# Botao ver Item
img_item = Image.open('item.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)
botao_ver = Button(frameMeio, command=ver_imagem, image=img_item, compound=LEFT, anchor=NW, text="   Ver item ".upper(), width=90, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_ver.place(x=330, y=219)

# Botao pesquisar
img_pesquisar = Image.open('lupa.png')
img_pesquisar = img_pesquisar.resize((20, 20))
img_pesquisar = ImageTk.PhotoImage(img_pesquisar)
botao_pesquisar = Button(frameMeio, command=pesquisar, image=img_pesquisar, compound=LEFT, anchor=NW, text=" Pesquisa ".upper(), width=90, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0 )
botao_pesquisar.place(x=330, y=10)


#########################################################################################################################################################

# funcao para mostrar
def mostrar():
    global tree
    # creating a treeview with dual scrollbars
    tabela_head = ['#Item', ' Código',  'OEM ', 'Descrição', 'Montadora',  ' Material', '  Peso ', 'Diâm. do gargalo', 'Diâm. bico maior', 'Diâm. bico menor']

    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)


    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=30)

    hd=["center","center","center","center","center","center","center", "center", "center","center"]
    h=[40,150,100,180,130,100,100, 100,120, 120]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)

        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


        mostrar()
janela.mainloop()

