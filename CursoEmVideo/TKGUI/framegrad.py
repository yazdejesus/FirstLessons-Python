import tkinter as gui

janela = gui.Tk()

frame = gui.Frame()
frame.pack()

ent_name = gui.Entry(master=frame, width=40)
ent_name.insert(0, "What is your name? ")
ent_name.pack()

janela.mainloop()