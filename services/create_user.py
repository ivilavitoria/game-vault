# Construa uma interface que simule uma tela de cadastro 
from services.mongo_service import save_user
import tkinter as tk
root = tk.Tk()

def openLoginPage():
    root.destroy()
    import app

def saveUser():
    name = str(make_name.get())
    email = str(make_email.get())
    password = str(make_password.get())

    save_user({
        "name": name,
        "email": email,
        "password": password
    })

    openLoginPage()

root.title("GameVault CREATE USER")
name = tk.Label(root, text = "Name: ")
name.place(x=10, y=50)

make_name = tk.Entry(root)
make_name.place(x=105, y=50)

email = tk.Label(root, text = "Email: ")
email.place(x=10, y=30)

make_email = tk.Entry(root)
make_email.place(x=105, y=30)

password = tk.Label(root, text = "Password: ")
password.place(x=10, y=70)

make_password = tk.Entry(root, show= "*")
make_password.place(x=105, y=70)

bt = tk.Button(root, text="Sign Up", command=saveUser)
bt.place(x=105, y=100)

root.geometry("800x400")
root.mainloop()

