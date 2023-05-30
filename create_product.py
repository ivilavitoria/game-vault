# crie uma tela de cadastro de produto(qualquer produto escolhido por você), onde ele possa criar, alterar, excluir ou consultar os produtos cadastrados.
from services.mongo_service import save_game
import tkinter as tk
root = tk.Tk()

def openListProduct():
    root.destroy()
    import list_product

def saveProduct():
    name = str(make_name.get())
    genre = str(make_genre.get())
    release = str(make_release.get())

    save_game({
        "name": name,
        "genre": genre,
        "release": release
    })

    openListProduct()

root.title("GameTracker CREATE GAMES")

lbl = tk.Label(root, text = "Name: ")
lbl.place(x=10, y=30)
make_name = tk.Entry(root)
make_name.place(x=105, y=30)

lbl = tk.Label(root, text = "Genre: ")
lbl.place(x=10, y=50)
make_genre = tk.Entry(root)
make_genre.place(x=105, y=50)

lbl = tk.Label(root, text = "Released at: ")
lbl.place(x=10, y=90)
make_release = tk.Entry(root)
make_release.place(x=105, y=90)

bt = tk.Button(root, text="Confirmar", command=saveProduct)
bt.place(x=105, y=160)

root.geometry("800x400")
root.mainloop()

