import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)
listaDeUsuariosCompleta = []


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

#Tela de login
class Toplevel1:

    def __init__(self, top=None):
        top = tk.Tk()        
        top.geometry("659x487")
        top.minsize(120, 1)
        top.maxsize(1924, 1041)
        top.resizable(1,  1)
        top.title("Interface de login e cadastro ")
        top.configure(background="#000000")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.197, rely=0.062, relheight=0.811, relwidth=0.616)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ff8000")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Label1 = tk.Label(self.Frame1)

        self.Label1.place(relx=0.394, rely=0.025, height=49, width=95)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ff8000")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Georgia} -size 21 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Login''')
        
        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.222, rely=0.228, height=39, width=105)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="#ff8000")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Georgia} -size 18 -weight bold")
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Usuário''')
        
        self.Label1_1_1 = tk.Label(self.Frame1)
        self.Label1_1_1.place(relx=0.222, rely=0.405, height=39, width=95)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(anchor='w')
        self.Label1_1_1.configure(background="#ff8000")
        self.Label1_1_1.configure(compound='left')
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Georgia} -size 18 -weight bold")
        self.Label1_1_1.configure(foreground="#ffffff")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text='''Senha''')
        
        self.Entry_usuario = tk.Entry(self.Frame1)
        self.Entry_usuario.place(relx=0.222, rely=0.329, height=30, relwidth=0.601)
        self.Entry_usuario.configure(background="white")
        self.Entry_usuario.configure(disabledforeground="#a3a3a3")
        self.Entry_usuario.configure(font="TkFixedFont")
        self.Entry_usuario.configure(foreground="#000000")
        self.Entry_usuario.configure(highlightbackground="#d9d9d9")
        self.Entry_usuario.configure(highlightcolor="black")
        self.Entry_usuario.configure(insertbackground="black")
        self.Entry_usuario.configure(selectbackground="#c4c4c4")
        self.Entry_usuario.configure(selectforeground="black")

        self.Entry_senha = tk.Entry(self.Frame1, show='*')
        self.Entry_senha.place(relx=0.222, rely=0.506, height=30, relwidth=0.601)
        self.Entry_senha.configure(background="white")
        self.Entry_senha.configure(disabledforeground="#a3a3a3")
        self.Entry_senha.configure(font="TkFixedFont")
        self.Entry_senha.configure(foreground="#000000")
        self.Entry_senha.configure(highlightbackground="#d9d9d9")
        self.Entry_senha.configure(highlightcolor="black")
        self.Entry_senha.configure(insertbackground="black")
        self.Entry_senha.configure(selectbackground="#c4c4c4")
        self.Entry_senha.configure(selectforeground="black")

        self.Button1 = tk.Button(self.Frame1, command=self.loginBackEnd)
        self.Button1.place(relx=0.222, rely=0.709, height=34, width=87)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#008000")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Georgia} -size 15")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')

        self.Button1_1 = tk.Button(self.Frame1, command=Cadastro)  
        self.Button1_1.place(relx=0.567, rely=0.709, height=34, width=97)
        self.Button1_1.configure(activebackground="beige")
        self.Button1_1.configure(activeforeground="black")
        self.Button1_1.configure(background="#008000")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Georgia} -size 15")
        self.Button1_1.configure(foreground="#ffffff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(relief="flat")
        self.Button1_1.configure(text='''Cadastrar''')
        
        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.498, rely=0.711,  relheight=0.071)
        self.TSeparator1.configure(orient="vertical")
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.top.mainloop()

# Função de login
    def loginBackEnd(self):

        with open ("usuarios.txt", 'r')as arquivosUsuario:
            usuarios = arquivosUsuario.readlines()
            usuarios = list(map(lambda x: x.replace('\n',''),usuarios)) 

            if len(usuarios) > 0 or len(usuarios) == 1:  
                listaDeUsuarios = usuarios

                for i in range(len(listaDeUsuarios)):
                    usuario = listaDeUsuarios[i].split("-")

                    usuarioDicionario = {"Nome": usuario[0], "Cpf": usuario[1]}

                    listaDeUsuariosCompleta.append(usuarioDicionario)


                usuarioEntrada = self.Entry_usuario.get()
                senhaEntrada = self.Entry_senha.get()
                logado = False
    
                if len(listaDeUsuariosCompleta) < 0:
                    print("Lista vazia")
                else:
                    for i in range(len(listaDeUsuariosCompleta)):
                        
                        if usuarioEntrada == listaDeUsuariosCompleta[i]['Nome'] and senhaEntrada == listaDeUsuariosCompleta[i]['Cpf']:
                            print('Usuário logado')
                            logado = True       
                if not logado:
                    print("Usuário e/ou senha incorreto")

        
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0

def _style_code():
       global _style_code_ran
       if _style_code_ran:
           return

       style = ttk.Style()
       if sys.platform == "win32":
           style.theme_use('winnative')
           style.configure('.',background=_bgcolor)
           style.configure('.',foreground=_fgcolor)
           style.configure('.',font='TkDefaultFont')
           style.map('.',background = [('selected', _compcolor), ('active',_ana2color)])
           if _bgmode == 'dark':
              style.map('.',foreground = [('selected', 'white'), ('active','white')])
           else:
            style.map('.',foreground = [('selected', 'black'), ('active','black')]) 
            style.map('TRadiobutton',background =[('selected', _bgcolor), ('active', _ana2color)], indicatorcolor = [('selected', _fgcolor), ('!active', _bgcolor)]) 
           _style_code_ran = 1
       
bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0

# Tela de cadastro
class Cadastro:
# Função de cadastro
     def cadastrarBackEnd(self):
        try:
            informacoes = f"{self.Entry_nome.get()}-{self.Entry_cpf.get()}"
            with open ("usuarios.txt", 'a')as arquivosUsuario:
                arquivosUsuario.write(informacoes + '\n')
                self.root.destroy()
        except:
            print("Houve um erro")


     def __init__(self, root = None):
                self.root = tk.Tk()
                self.root.geometry("692x464+469+217")
                self.root.minsize(120, 1)
                self.root.maxsize(1924, 1061)
                self.root.resizable(1,  1)
                self.root.title("Realizar/ Atualiar cadastro")
                self.root.configure(background="#000000")
                self.root = self.root

                self.Frame1 = tk.Frame(self.root)
                self.Frame1.place(relx=0.014, rely=0.022, relheight=0.938 , relwidth=0.974)
                self.Frame1.configure(relief='groove')
                self.Frame1.configure(borderwidth="2")
                self.Frame1.configure(relief="groove")
                self.Frame1.configure(background="#d9d9d9")

                self.nome = tk.Label(self.Frame1)
                self.nome.place(relx=0.015, rely=0.126, height=31, width=64)
                self.nome.configure(anchor='w')
                self.nome.configure(background="#d9d9d9")
                self.nome.configure(compound='left')
                self.nome.configure(cursor="fleur")
                self.nome.configure(disabledforeground="#a3a3a3")
                self.nome.configure(foreground="#000000")
                self.nome.configure(text='''Nome:''')

                self.endereco = tk.Label(self.Frame1)
                self.endereco.place(relx=0.015, rely=0.218, height=31, width=64)
                self.endereco.configure(activebackground="#f9f9f9")
                self.endereco.configure(anchor='w')
                self.endereco.configure(background="#d9d9d9")
                self.endereco.configure(compound='left')
                self.endereco.configure(cursor="fleur")
                self.endereco.configure(disabledforeground="#a3a3a3")
                self.endereco.configure(foreground="#000000")
                self.endereco.configure(highlightbackground="#d9d9d9")
                self.endereco.configure(highlightcolor="black")
                self.endereco.configure(text='''Endereço:''')

                self.Entry_nome = tk.Entry(self.Frame1)
                self.Entry_nome.place(relx=0.089, rely=0.138, height=20, relwidth=0.51)
                self.Entry_nome.configure(background="white")
                self.Entry_nome.configure(disabledforeground="#a3a3a3")
                self.Entry_nome.configure(font="TkFixedFont")
                self.Entry_nome.configure(foreground="#000000")
                self.Entry_nome.configure(insertbackground="black")

                self.Entry_endereco = tk.Entry(self.Frame1)
                self.Entry_endereco.place(relx=0.104, rely=0.23, height=20, relwidth=0.51)
                self.Entry_endereco.configure(background="white")
                self.Entry_endereco.configure(disabledforeground="#a3a3a3")
                self.Entry_endereco.configure(font="TkFixedFont")
                self.Entry_endereco.configure(foreground="#000000")
                self.Entry_endereco.configure(highlightbackground="#d9d9d9")
                self.Entry_endereco.configure(highlightcolor="black")
                self.Entry_endereco.configure(insertbackground="black")
                self.Entry_endereco.configure(selectbackground="#c4c4c4")
                self.Entry_endereco.configure(selectforeground="black")

                self.titulo_cadastro = tk.Label(self.Frame1)
                self.titulo_cadastro.place(relx=0.415, rely=0.023, height=21, width=214)
                self.titulo_cadastro.configure(anchor='w')
                self.titulo_cadastro.configure(background="#d9d9d9")
                self.titulo_cadastro.configure(compound='left')
                self.titulo_cadastro.configure(disabledforeground="#a3a3a3")
                self.titulo_cadastro.configure(font="-family {Georgia} -size 20 -weight bold -slant italic")
                self.titulo_cadastro.configure(foreground="#000000")
                self.titulo_cadastro.configure(text='''Cadastro''')

                self.email = tk.Label(self.Frame1)
                self.email.place(relx=0.015, rely=0.402, height=31, width=64)
                self.email.configure(activebackground="#f9f9f9")
                self.email.configure(anchor='w')
                self.email.configure(background="#d9d9d9")
                self.email.configure(compound='left')
                self.email.configure(disabledforeground="#a3a3a3")
                self.email.configure(foreground="#000000")
                self.email.configure(highlightbackground="#d9d9d9")
                self.email.configure(highlightcolor="black")
                self.email.configure(text='''Email:''')

                self.Entry_email = tk.Entry(self.Frame1)
                self.Entry_email.place(relx=0.089, rely=0.414, height=20, relwidth=0.525)
                self.Entry_email.configure(background="white")
                self.Entry_email.configure(disabledforeground="#a3a3a3")
                self.Entry_email.configure(font="TkFixedFont")
                self.Entry_email.configure(foreground="#000000")
                self.Entry_email.configure(highlightbackground="#d9d9d9")
                self.Entry_email.configure(highlightcolor="black")
                self.Entry_email.configure(insertbackground="black")
                self.Entry_email.configure(selectbackground="#c4c4c4")
                self.Entry_email.configure(selectforeground="black")

                self.cpf = tk.Label(self.Frame1)
                self.cpf.place(relx=0.638, rely=0.126, height=31, width=64)
                self.cpf.configure(activebackground="#f9f9f9")
                self.cpf.configure(anchor='w')
                self.cpf.configure(background="#d9d9d9")
                self.cpf.configure(compound='left')
                self.cpf.configure(disabledforeground="#a3a3a3")
                self.cpf.configure(foreground="#000000")
                self.cpf.configure(highlightbackground="#d9d9d9")
                self.cpf.configure(highlightcolor="black")
                self.cpf.configure(text='''Cpf:''')

                self.Entry_cpf = tk.Entry(self.Frame1)
                self.Entry_cpf.place(relx=0.697, rely=0.138, height=20, relwidth=0.243)
                self.Entry_cpf.configure(background="white")
                self.Entry_cpf.configure(disabledforeground="#a3a3a3")
                self.Entry_cpf.configure(font="TkFixedFont")
                self.Entry_cpf.configure(foreground="#000000")
                self.Entry_cpf.configure(highlightbackground="#d9d9d9")
                self.Entry_cpf.configure(highlightcolor="black")
                self.Entry_cpf.configure(insertbackground="black")
                self.Entry_cpf.configure(selectbackground="#c4c4c4")
                self.Entry_cpf.configure(selectforeground="black")

                self.teelefone = tk.Label(self.Frame1)
                self.teelefone.place(relx=0.638, rely=0.402, height=31, width=64)
                self.teelefone.configure(activebackground="#f9f9f9")
                self.teelefone.configure(anchor='w')
                self.teelefone.configure(background="#d9d9d9")
                self.teelefone.configure(compound='left')
                self.teelefone.configure(disabledforeground="#a3a3a3")
                self.teelefone.configure(foreground="#000000")
                self.teelefone.configure(highlightbackground="#d9d9d9")
                self.teelefone.configure(highlightcolor="black")
                self.teelefone.configure(text='''Telefone:''')

                self.Entry_telefone = tk.Entry(self.Frame1)
                self.Entry_telefone.place(relx=0.727, rely=0.414, height=20, relwidth=0.214)
                self.Entry_telefone.configure(background="white")
                self.Entry_telefone.configure(disabledforeground="#a3a3a3")
                self.Entry_telefone.configure(font="TkFixedFont")
                self.Entry_telefone.configure(foreground="#000000")
                self.Entry_telefone.configure(highlightbackground="#d9d9d9")
                self.Entry_telefone.configure(highlightcolor="black")
                self.Entry_telefone.configure(insertbackground="black")
                self.Entry_telefone.configure(selectbackground="#c4c4c4")
                self.Entry_telefone.configure(selectforeground="black")

                self.CEP = tk.Label(self.Frame1)
                self.CEP.place(relx=0.653, rely=0.218, height=31, width=64)
                self.CEP.configure(activebackground="#f9f9f9")
                self.CEP.configure(anchor='w')
                self.CEP.configure(background="#d9d9d9")
                self.CEP.configure(compound='left')
                self.CEP.configure(disabledforeground="#a3a3a3")
                self.CEP.configure(foreground="#000000")
                self.CEP.configure(highlightbackground="#d9d9d9")
                self.CEP.configure(highlightcolor="black")
                self.CEP.configure(text='''CEP:''')

                self.Entry_cep = tk.Entry(self.Frame1)
                self.Entry_cep.place(relx=0.697, rely=0.23, height=20, relwidth=0.243)
                self.Entry_cep.configure(background="white")
                self.Entry_cep.configure(disabledforeground="#a3a3a3")
                self.Entry_cep.configure(font="TkFixedFont")
                self.Entry_cep.configure(foreground="#000000")
                self.Entry_cep.configure(highlightbackground="#d9d9d9")
                self.Entry_cep.configure(highlightcolor="black")
                self.Entry_cep.configure(insertbackground="black")
                self.Entry_cep.configure(selectbackground="#c4c4c4")
                self.Entry_cep.configure(selectforeground="black")

                self.Estado = tk.Label(self.Frame1)
                self.Estado.place(relx=0.015, rely=0.31, height=31, width=64)
                self.Estado.configure(activebackground="#f9f9f9")
                self.Estado.configure(anchor='w')
                self.Estado.configure(background="#d9d9d9")
                self.Estado.configure(compound='left')
                self.Estado.configure(cursor="fleur")
                self.Estado.configure(disabledforeground="#a3a3a3")
                self.Estado.configure(foreground="#000000")
                self.Estado.configure(highlightbackground="#d9d9d9")
                self.Estado.configure(highlightcolor="black")
                self.Estado.configure(text='''Estado:''')

                self.Entry_estado = tk.Entry(self.Frame1)
                self.Entry_estado.place(relx=0.089, rely=0.322, height=20, relwidth=0.228)
                self.Entry_estado.configure(background="white")
                self.Entry_estado.configure(disabledforeground="#a3a3a3")
                self.Entry_estado.configure(font="TkFixedFont")
                self.Entry_estado.configure(foreground="#000000")
                self.Entry_estado.configure(highlightbackground="#d9d9d9")
                self.Entry_estado.configure(highlightcolor="black")
                self.Entry_estado.configure(insertbackground="black")
                self.Entry_estado.configure(selectbackground="#c4c4c4")
                self.Entry_estado.configure(selectforeground="black")

                self.Cidade = tk.Label(self.Frame1)
                self.Cidade.place(relx=0.341, rely=0.31, height=31, width=64)
                self.Cidade.configure(activebackground="#f9f9f9")
                self.Cidade.configure(anchor='w')
                self.Cidade.configure(background="#d9d9d9")
                self.Cidade.configure(compound='left')
                self.Cidade.configure(disabledforeground="#a3a3a3")
                self.Cidade.configure(foreground="#000000")
                self.Cidade.configure(highlightbackground="#d9d9d9")
                self.Cidade.configure(highlightcolor="black")
                self.Cidade.configure(text='''Cidade:''')

                self.Entry_cidade = tk.Entry(self.Frame1)
                self.Entry_cidade.place(relx=0.43, rely=0.322, height=20, relwidth=0.214)
                self.Entry_cidade.configure(background="white")
                self.Entry_cidade.configure(disabledforeground="#a3a3a3")
                self.Entry_cidade.configure(font="TkFixedFont")
                self.Entry_cidade.configure(foreground="#000000")
                self.Entry_cidade.configure(highlightbackground="#d9d9d9")
                self.Entry_cidade.configure(highlightcolor="black")
                self.Entry_cidade.configure(insertbackground="black")
                self.Entry_cidade.configure(selectbackground="#c4c4c4")
                self.Entry_cidade.configure(selectforeground="black")

                self.Bairro = tk.Label(self.Frame1)
                self.Bairro.place(relx=0.653, rely=0.31, height=31, width=64)
                self.Bairro.configure(activebackground="#f9f9f9")
                self.Bairro.configure(anchor='w')
                self.Bairro.configure(background="#d9d9d9")
                self.Bairro.configure(compound='left')
                self.Bairro.configure(disabledforeground="#a3a3a3")
                self.Bairro.configure(foreground="#000000")
                self.Bairro.configure(highlightbackground="#d9d9d9")
                self.Bairro.configure(highlightcolor="black")
                self.Bairro.configure(text='''Bairro:''')

                self.Entry_bairro = tk.Entry(self.Frame1)
                self.Entry_bairro.place(relx=0.712, rely=0.322, height=20 , relwidth=0.228)
                self.Entry_bairro.configure(background="white")
                self.Entry_bairro.configure(disabledforeground="#a3a3a3")
                self.Entry_bairro.configure(font="TkFixedFont")
                self.Entry_bairro.configure(foreground="#000000")
                self.Entry_bairro.configure(highlightbackground="#d9d9d9")
                self.Entry_bairro.configure(highlightcolor="black")
                self.Entry_bairro.configure(insertbackground="black")
                self.Entry_bairro.configure(selectbackground="#c4c4c4")
                self.Entry_bairro.configure(selectforeground="black")
                
                self.Confirmar_cadastro = tk.Button(self.Frame1,command=self.cadastrarBackEnd)
                self.Confirmar_cadastro.place(relx=0.49, rely=0.69, height=34, width=157)
                self.Confirmar_cadastro.configure(activebackground="beige")
                self.Confirmar_cadastro.configure(activeforeground="black")
                self.Confirmar_cadastro.configure(background="#008000")
                self.Confirmar_cadastro.configure(compound='left')
                self.Confirmar_cadastro.configure(disabledforeground="#a3a3a3")
                self.Confirmar_cadastro.configure(foreground="#ffffff")
                self.Confirmar_cadastro.configure(highlightbackground="#d9d9d9")
                self.Confirmar_cadastro.configure(highlightcolor="black")
                self.Confirmar_cadastro.configure(pady="0")
                self.Confirmar_cadastro.configure(text='''Cadastrar''')

            
                self.excluir_cadastro = tk.Button(self.Frame1)
                self.excluir_cadastro.place(relx=0.208, rely=0.69, height=34, width=157)
                self.excluir_cadastro.configure(activebackground="beige")
                self.excluir_cadastro.configure(activeforeground="black")
                self.excluir_cadastro.configure(background="#ff0000")
                self.excluir_cadastro.configure(compound='left')
                self.excluir_cadastro.configure(cursor="fleur")
                self.excluir_cadastro.configure(disabledforeground="#a3a3a3")
                self.excluir_cadastro.configure(foreground="#ffffff")
                self.excluir_cadastro.configure(highlightbackground="#d9d9d9")
                self.excluir_cadastro.configure(highlightcolor="black")
                self.excluir_cadastro.configure(pady="0")
                self.excluir_cadastro.configure(text='''Excluir''')
                self.root.mainloop()
Toplevel1()
