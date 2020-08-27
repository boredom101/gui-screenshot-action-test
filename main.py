import tkinter

top = tkinter.Tk()

var = tkinter.StringVar()
label = tkinter.Label( root, textvariable = var, relief = tkinter.RAISED )

var.set("Hey!? How are you doing?")
label.pack()

top.mainloop()

