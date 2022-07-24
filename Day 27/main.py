from tkinter import *
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width = 500, height = 200)
window.config(padx = 50, pady = 50)


entry = Entry(width=10)
entry.insert(END, string = "0")
entry.grid(column = 20, row = 16)
num = int(entry.get())


def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    label_3.config(text= f"{km}")
    

button = Button(text = "Calculate", command = calculate)
button.grid(column = 20, row = 40)




label = Label()
label.config(text="Miles")
label.grid(column = 30, row = 16)

label_1 = Label()
label_1.config(text = "is equal to")
label_1.grid(column = 15, row = 30)

label_2 = Label()
label_2.config(text = "Km")
label_2.grid(column = 25,row = 30)

label_3 = Label(text="0")
label_3.grid(column = 20, row = 30)

window.mainloop()