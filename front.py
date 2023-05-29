# Construa uma interface que simule uma tela de login de usuário contendo o campo de login, senha e um botão de autenticação.
from tkinter import *

def confirma_clica():
    login= str(campo_login.get())
    password = str(password.get())
    if login == "Estacio" and password == "python":
        print("Login Ok")
        lb2 = Label(janela, text= "Login Ok", font= "Ivy20", bg="green")
        lb2.place(x=55, y=80)

    else:
        print("Incorrect Password")
        lb3 = Label(text= "Incorrect Password", bg= "red")
        lb3.place(x=55, y=80)

janela = Tk()
janela.title('GameTracker')
lbl = Label(janela, text = 'Login: ')
lbl.place(x=10, y=10)

campo_login = Entry(janela)
campo_login.place(x=55, y=10)

senha = Label(janela, text = 'Senha: ')
senha.place(x=10, y=35)

campo_senha = Entry(janela, show= '*')
campo_senha.place(x=55, y=35)

bt = Button(janela, text='Confirmar', command=confirma_clica)
bt.place(x=55, y=55)

janela.geometry('400x400')
janela.mainloop()
