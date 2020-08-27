top = tkinter.Tk()

var = StringVar()
label = Label( root, textvariable = var, relief = RAISED )

var.set("Hey!? How are you doing?")
label.pack()

top.mainloop()

