from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dados import *

# Cores
cor01 = '#2e2d2b'   # Preta
cor02 = '#d3d3d3'   # Cinza Claro
cor03 = '#feffff'   # Branca
cor04 = '#4fa882'   # Verde
cor05 = '#38576b'   # valor
cor06 = '#403d3d'   # letra
cor07 = '#e06636'   # - profit
cor08 = '#038cfc'   # azul
cor09 = '#3fbfb9'   # verde
cor10 = '#FF0430'   # vermelha
cor11 = '#e9edf5'   # + verde
cor12 = '#274360'   # azul marinho

# Criando Janela

janela = Tk()
janela.title('')
janela.geometry('500x450')
janela.configure(background=cor02)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# # Criando frames

frame_cima = Frame(janela, width=500, height=50, bg=cor12, relief=FLAT)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=cor02, relief=FLAT)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=248, bg=cor03, relief=FLAT)
frame_tabela.grid(row=2, column=0, columnspan=2, pady=1, padx=10, sticky=NW)

# configuração do frame de cima

l_nome = Label(frame_cima, text='AGENDA TELEFÔNICA', anchor=NE, font='times 20 bold', bg=cor12, fg=cor02)
l_nome.place(x=100, y=5)

l_linha = Label(frame_cima, text='', width=500, anchor=NE, font='times 1', bg=cor03, fg=cor02)
l_linha.place(x=0, y=46)


global tree
# Configuração frame Tabela e das funções dos botões ---------------------------


# Funções da tabela
def mostrar_dados():
    global tree
    # Criando a tabela
    cabecalho = ['Nome', 'Sexo', 'Telefone', 'email']

    dados = ver_dados()

    tree = ttk.Treeview(frame_tabela, selectmode='extended', columns=cabecalho, show='headings')

    # Scrollbar vertical
    vsb = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)

    # Scrollbar Horizontal
    hsb = ttk.Scrollbar(frame_tabela, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # Tree cabeçalho

    tree.heading(0, text='Nome', anchor=NW)
    tree.heading(1, text='Sexo', anchor=NW)
    tree.heading(2, text='Telefone', anchor=NW)
    tree.heading(3, text='E-mail', anchor=NW)

    # Tree Corpo

    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=100, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(0, width=120, anchor='nw')

    for item in dados:
        tree.insert('', 'end', values=item)


# Função mostrar
mostrar_dados()


# Função add
def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_tel.get()
    email = e_email.get()
    dados = [nome, sexo, telefone, email]
    if nome == '' or sexo == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'Por favor preencha todos os campos')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Dados inseridos com sucesso')
        # Deletando os campos para a proxima entrada de dados
        e_nome.delete(0, 'end')
        c_sexo.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')

        mostrar_dados()


# Função Atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        nome = tree_lista[0]
        sexo = tree_lista[1]
        telefone = str(tree_lista[2])
        email = tree_lista[3]

        e_nome.insert(0, nome)
        c_sexo.insert(0, sexo)
        e_tel.insert(0, telefone)
        e_email.insert(0, email)

        def confirmar():

            nome = e_nome.get()
            sexo = c_sexo.get()
            telefone = e_tel.get()
            email = e_email.get()

            dados = [telefone, nome, sexo, telefone, email]

            atualizar_dados(dados)

            messagebox.showinfo('Dados', 'Dados foram atualizados com sucesso')

            # Deletando os campos para a proxima entrada de dados
            e_nome.delete(0, 'end')
            c_sexo.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_email.delete(0, 'end')

            b_confirmar.destroy()

            mostrar_dados()

        b_confirmar = Button(frame_baixo, command=confirmar, text='Confirmar', width=10, font='Ivy 8 bold', bg=cor09,
                             fg=cor06, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=80)
    except:
        messagebox.showwarning('Dados', 'Por favor selecione uma informação na tabela')


# Função Remover
def remover():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        telefone = str(tree_lista[2])
        remover_dados(telefone)
        messagebox.showinfo('Dados', 'Dados foram removidos com sucesso')
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        mostrar_dados()

    except:
        messagebox.showwarning('Dados', 'Por favor selecione uma informação na tabela')


# Função pesquisar
def procurar():
    nome = e_procurar.get()
    dados = pesquisar_dados(nome)
    tree.delete(*tree.get_children())
    for item in dados:
        tree.insert('', 'end', values=item)


# Configuração do frame de baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font='Ivy 10', bg=cor02, fg=cor06)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('', 10), highlightthickness=1)
e_nome.place(x=80, y=20)

l_sexo = Label(frame_baixo, text='Sexo *', anchor=NW, font='Ivy 10', bg=cor02, fg=cor06)
l_sexo.place(x=10, y=50)
c_sexo = Combobox(frame_baixo, width=27)
c_sexo['value'] = ('', 'FEMININO', 'MASCULINO')
c_sexo.place(x=80, y=50)

l_tel = Label(frame_baixo, text='Telefone *', anchor=NW, font='Ivy 10', bg=cor02, fg=cor06)
l_tel.place(x=10, y=80)
e_tel = Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('', 10), highlightthickness=1)
e_tel.place(x=80, y=80)

l_email = Label(frame_baixo, text='E-mail *', anchor=NW, font='Ivy 10', bg=cor02, fg=cor06)
l_email.place(x=10, y=110)
e_email = Entry(frame_baixo, width=25, justify='left', relief=FLAT, font=('', 10), highlightthickness=1)
e_email.place(x=80, y=110)


# Criação dos botões
b_procurar = Button(frame_baixo, command=procurar, text='Procurar', font='Ivy 8 bold', bg=cor02, fg=cor06,
                    relief=RAISED, overrelief=RIDGE)
b_procurar.place(x=290, y=20)
e_procurar = Entry(frame_baixo, width=16, justify='left', font=('', 11), highlightthickness=1)
e_procurar.place(x=347, y=21)

b_ver = Button(frame_baixo, command=mostrar_dados, text='Ver dados', width=10, font='Ivy 8 bold', bg=cor11, fg=cor06,
               relief=RAISED, overrelief=RIDGE)
b_ver.place(x=290, y=50)

b_adicionar = Button(frame_baixo, command=inserir, text='Adicionar', width=10, font='Ivy 8 bold', bg=cor04, fg=cor06,
                     relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=415, y=50)

b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font='Ivy 8 bold', bg=cor09, fg=cor06,
                     relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=415, y=80)

b_deletar = Button(frame_baixo, command=remover, text='Deletar', width=10, font='Ivy 8 bold', bg=cor10, fg=cor06,
                   relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=415, y=110)


janela.mainloop()

