
from tkinter import *


# create window
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=400, height=200)
window.config(padx=40, pady=40)

# label
is_equal_label = Label(text="is equal to", font=("Arial", 16))
is_equal_label.grid(column=0, row=1)


miles = Label(text="Miles", font=("Arial", 16))
miles.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 16))
km_label.grid(column=2, row=1)

converted_int_label = Label(text="0", font=("Arial", 16))
converted_int_label.grid(column=1, row=1)


# Button


def button_clicked():
    miles = input.get()
    km = float(miles) * 1.60934
    converted_int_label.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked, font=("Arial", 16))
button.grid(column=1, row=2)


# Entry component
input = Entry(width=5, font=("Arial", 16))
input.focus()
input.grid(column=1, row=0)


window.mainloop()
