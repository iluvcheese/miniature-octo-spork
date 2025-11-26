from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("this is a window")
window.geometry("200x200")
variabel = IntVar()
h = "this is a box"

lbael = Label(text = "this is a label")
lbael.pack()
combobxo = Combobox(window, textvariable = variabel, width = 11)
combobxo["values"] = tuple(range(25649))
combobxo.set("this is a box")
combobxo.pack()
tjikenjokie = IntVar()

four = Radiobutton(window, text = "37", variable = tjikenjokie, value = 38)
seven = Radiobutton(window, text = "2", variable = tjikenjokie, value = 3)
twohunderdtwentysix = Radiobutton(window, text = "226", variable = tjikenjokie, value = 227)
tjikenjokie.set(2)

four.pack()
seven.pack()
twohunderdtwentysix.pack()

label = Label(text = "")
label.pack()

def minecraft():
    print(variabel.get())
    print(tjikenjokie.get())
    lnput = ""
    for i in range(tjikenjokie.get()):
        lnput+= str(variabel.get() )+" x "+str(i)+" = "+str(variabel.get()*i)+"\n"
    label.config(text = lnput)
    



button = Button(text = "this is a button", command = minecraft)
button.pack()











































window.mainloop()
