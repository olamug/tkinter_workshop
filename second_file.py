import tkinter
from tkinter.messagebox import *
from tkinter.filedialog import *

top = tkinter.Tk()


def print_text(ent):
    # print(ent.get()) pierwsza wersja przyjmowania i printowania wprowadzonego obiektu do entry
    tkinter.messagebox.showinfo('Informacja', ent.get())


entry1=tkinter.Entry(top, width=50)
entry1.pack(side='left')

button_print = tkinter.Button(top, text='Print text', command=lambda: print_text(entry1))
button_print.pack(side='left')

top.mainloop()