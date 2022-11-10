from tkinter import *


def button_clicked():
    if option.get() == "mi to km":
        miles = input.get()
        km = round(float(miles) * 1.609344, 3)
        calculated_label.config(text=km)
    elif option.get() == "km to mi":
        km = input.get()
        miles = round(float(km) / 1.609344, 3)
        calculated_label.config(text=miles)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

first_label_mi = Label(text="mi")
first_label_mi.grid(column=2, row=1)

second_label_km = Label(text="km")
second_label_km.grid(column=2, row=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=2)

calculated_label = Label(text="0")
calculated_label.grid(column=1, row=2)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=3)

input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=1)

option = StringVar()

options = [
    "mi to km",
    "km to mi"
]


def mi_or_km(*args):
    if option.get() == "mi to km":
        first_label_mi.config(text="mi")
        second_label_km.config(text="km")
    elif option.get() == "km to mi":
        first_label_mi.config(text="km")
        second_label_km.config(text="mi")


option_select = OptionMenu(window, option, *options)
option.trace("w", mi_or_km)
option.set(options[0])
option_select.grid(column=1, row=0)

window.mainloop()
