from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

root = Tk()

root.title("Web aplikacija")
root.configure(background="light blue")
root.geometry("800x600")
root.resizable(width=False, height=False)

Naslov_label = ttk.Label(root, text="Naslov", background="light blue", font=("TkMenuFont", 16))
Naslov_label.grid(row=0, column=0, sticky=W)
Naslov_text = StringVar()
Naslov_entry = ttk.Entry(root,width=24,textvariable=Naslov_text)
Naslov_entry.grid(row=0, column=1, sticky=W)

Autor_label = ttk.Label(root, text="Autor", background="light blue", font=("TkMenuFont", 16))
Autor_label.grid(row=0, column=2, sticky=W)
Autor_text = StringVar()
Autor_entry = ttk.Entry(root,width=24,textvariable=Autor_text)
Autor_entry.grid(row=0, column=3, sticky=W)

Serijski_broj_label = ttk.Label(root, text="Serijski broj", background="light blue", font=("TkMenuFont", 16))
Serijski_broj_label.grid(row=0, column=4, sticky=W)
Serijski_broj_text = StringVar()
Serijski_broj_entry = ttk.Entry(root,width=24,textvariable=Serijski_broj_text)
Serijski_broj_entry.grid(row=0, column=5, sticky=W)

add_btn = Button(root, text="Dodaj podatke", bg="navy blue", fg="white", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=6, sticky=W)

list_bx = Listbox(root, height=16, width=40, font="helvetica 13", bg="light yellow")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)

list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

Izmijeni_btn = Button(root, text="Izmijeni podatke", bg="orange", fg="black", font="helvetica 10 bold", command="")
Izmijeni_btn.grid(row=15, column=4)

Obrisi_btn = Button(root, text="Obrisi podatke", bg="red", fg="black", font="helvetica 10 bold", command="")
Obrisi_btn.grid(row=15, column=2)

root.mainloop()
