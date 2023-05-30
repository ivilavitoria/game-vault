# crie uma tela de cadastro de produto(qualquer produto escolhido por você), onde ele possa criar, alterar, excluir ou consultar os produtos cadastrados.
from services.mongo_service import list_games, delete_game
import tkinter as tk
from tkinter import ttk
root = tk.Tk()

def openCreateProduct():
    root.destroy()
    import create_product

def deleteProduct():
    curItem = tree.focus()
    id = tree.item(curItem)["values"][0]
    delete_game(id)
    selectedItem = tree.selection()[0]
    tree.delete(selectedItem)

root.title("GameTracker LIST GAMES")

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings', height=5)

tree.column("# 1", anchor="center")
tree.heading("# 1", text="ID")
tree.column("# 2", anchor="center")
tree.heading("# 2", text="Name")
tree.column("# 3", anchor="center")
tree.heading("# 3", text="Genre")
tree.column("# 4", anchor="center")
tree.heading("# 4", text="Released at")

games = list_games()

index = 1
for item in games:
    id = item["_id"]
    name = item["name"]
    genre = item["genre"]
    release = item["release"]

    tree.insert('', 'end', text=index, values=(id, name, genre, release))
    index += 1

tree.pack()

bt = tk.Button(root, text="Create New Product", command=openCreateProduct)
bt.place(x=105, y=160)

bt = tk.Button(root, text="Delete Product", command=deleteProduct)
bt.place(x=250, y=160)

root.geometry("800x400")
root.mainloop()

