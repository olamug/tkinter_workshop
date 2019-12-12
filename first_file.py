import tkinter
from tkinter.colorchooser import *


def color_label(lab):
    color = tkinter.colorchooser.askcolor(parent=top)  # parent to jest przypisanie, że chodzi o top-główne okno
    print(color)
    lab.configure(bg=color[1])


top = tkinter.Tk()
top.wm_title('Hello...')

top.resizable(width='false', height='false')  # tutaj uzytkownik będzie mógl sobie rozciągać i ustalać dowoli rozmiar
# top.minsize(width=200, height=50)
# top.maxsize(width=200, height=50)

#dodawanie ramki
frame1 = tkinter.Frame(top, borderwidth=2, relief='ridge', pady=4, padx=4)
# frame1.pack(fill='y', side='left')
frame1.grid(row=0, column=0, sticky='ns')

frame2 = tkinter.Frame(top, borderwidth=2, relief='ridge', pady=4, padx=4)
# frame2.pack(fill='y', side='left')
frame2.grid(row=0, column=1, sticky='ns')

frame3 = tkinter.Frame(top, borderwidth=2, relief='ridge', pady=4, padx=4)
# frame3.pack(fill='y', side='left')
frame3.grid(row=1, column=0, sticky='ew', columnspan=2)


label1 = tkinter.Label(frame1, text='...world')
label1.pack()  # komenda umieszczająca dany element w naszym oknie. coś tworzymy - pakujemy na koniec


b_close = tkinter.Button(frame2, text='Zamknij', command=top.destroy)
b_close.pack()  # fill='x'rozciągnięcie rozmiaru elementu w danym wymiarze, tutaj button jest na szerokość osi x


b_color = tkinter.Button(frame3, text='Kolor', command=lambda: color_label(label1))
b_color.pack(fill='x')


top.mainloop()
