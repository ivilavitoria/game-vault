# Construa uma interface que simule uma tela de login de usuário contendo o campo de login, senha e um botão de autenticação.
from services.mongo_service import get_user
import tkinter as tk
root = tk.Tk()

def openCreateUser():
    root.destroy()
    import services.create_user

def openCreateProduct():
    root.destroy()
    import services.list_product


def login():
    login = str(make_login.get())
    password = str(make_password.get())
    user = get_user(login)

    if user != None:
        if user["password"] != password:
            lb2 = tk.Label(text= "Incorrect Password", bg= "red")
            lb2.place(x=55, y=80)
            return
        else: 
            openCreateProduct()
    else: 
        lb3 = tk.Label(text= "User don't exists", bg= "red")
        lb3.place(x=55, y=80)
        return

root.title("GameVault")
lbl = tk.Label(root, text = "Email: ")
lbl.place(x=10, y=10)

make_login = tk.Entry(root)
make_login.place(x=75, y=10)

lbl = tk.Label(root, text = "Password: ")
lbl.place(x=10, y=35)

make_password = tk.Entry(root, show= "*")
make_password.place(x=75, y=35)

bt = tk.Button(root, text="Sign In", command=login)
bt.place(x=75, y=65)

bt = tk.Button(root, text="Sign Up", command=openCreateUser)
bt.place(x=75, y=100)

root.geometry("800x400")
root.mainloop()


