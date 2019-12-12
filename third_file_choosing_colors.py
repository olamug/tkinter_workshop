import tkinter

top = tkinter.Tk()


colors = [('Red', 'red'),
          ('Green', 'green'),
          ('Blue', 'blue'),
          ('White', 'white')]

v = tkinter.StringVar()
v.set('red')

for text, color in colors:
    b = tkinter.Radiobutton(top, text=text, variable=v, value=color)
    b.pack(anchor='w')


def color_button():
    button_color.configure(bg=v.get())


button_color = tkinter.Button(top, text='COLOR ME', command=color_button)
button_color.pack(side='bottom', fill='x')


top.mainloop()
