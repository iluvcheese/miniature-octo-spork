from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("khjgkjhsgfhfglsdfkbgfjgfdlbsdfgkjdgfsvkjdfghmfdjfvkjfdvgkjhdfbkjgfhbdjhbgkjdfbgkfdsbgkjdbsfkjgbsdfbkjdsgfgjdhbkjhhkgvkgvkgvkgvkvkjgvkjgvkvjkvjvkjvdjkhfsbjfhbkgbfkfbsdjhbkjhdgfbkfbdkshbgkjhsdbfgjksdbfjhgbkjsdfbbgkdsfjvfgmbdfjhvbcv khdfhcbvkskvscjvjkdhsjgcvgjbdjsvcx dxhcvkhsxbdkjgxcjgvjhdgskhvxcvhxbhcvhdxcjhvdxkjcvkhxhdvhbdxhvhchvbdxjgvcvjxdgvcvjxgcvx  dhvbdxjbvhxbvhcbhdxbjgbdkhgbhnmn")
window.geometry("200x200")
variabel = IntVar()
h = "this is a box"

lbael = Label(text = "this is a label")
lbael.pack()
combobxo = Combobox(window, textvariable = variabel, width = 11)
combobxo["values"] = ["this is a box", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
"31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
"41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
"51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
"61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
"71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
"81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
"91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
combobxo.set("this is a box")
combobxo.pack()

four = Radiobutton(window, text = "37")
seven = Radiobutton(window, text = "2")
twohunderdtwentysix = Radiobutton(window, text = "226")
four.pack()
seven.pack()
twohunderdtwentysix.pack()










































window.mainloop()