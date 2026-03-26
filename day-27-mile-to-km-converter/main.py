from tkinter import *

FONT = ("Arial", 10, "normal")
PADDING = {"padx": 5, "pady": 15}

def button_clicked(label):
    miles = float(input.get())
    km = round(miles * 1.609, 2)
    label.config(text=str(km))

#### Window ####

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=30)
window.config(padx=50, pady=20)

#### Label ####

miles_label = Label(text="Miles", font=FONT, **PADDING)
miles_label.grid(column=1, row=0)

km_label = Label(text="Km", font=FONT, **PADDING)
km_label.grid(column=4, row=0)

equal_label = Label(text="=", font=FONT, **PADDING)
equal_label.grid(column=2, row=0)

result_label = Label(text="0", width=7, font=("Arial", 10, "bold"), **PADDING, anchor="e")
result_label.grid(column=3, row=0)

#### Button ####

button = Button(text = "Calculate", command=lambda:button_clicked(result_label), font=FONT)
button.grid(column=0, row=1)

#### Entry ####

input = Entry(width=10, font=FONT, justify="right")
input.get()
input.grid(column=0, row=0)

#### Exit ####

window.mainloop()