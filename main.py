from tkinter import *


def button_clicked():
    miles = miles_input.get()
    km = round(int(miles) * 1.609344, 3)
    calculated_km_label.config(text=km)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

calculated_km_label = Label(text="0")
calculated_km_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

window.mainloop()
