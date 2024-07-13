from  tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

input_field = Entry(width=10)
input_field.grid(column=1, row=0)

my_label = Label(text="Miles", font=("Arial", 15, "bold"))
my_label.grid(column=2, row=0)

my_label = Label(text="Km", font=("Arial", 15, "bold"))
my_label.grid(column=2, row=1)

my_label_1 = Label(text=" ", font=("Arial", 15, "bold"))
my_label_1.grid(column=1, row=1)

def miles_to_km():
    miles = float(input_field.get())
    km = round(miles * 1.60934)
    my_label_1.config(text=f"{km}")


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)





my_label_2 = Label(text="Is equal to", font=("Arial", 15, "bold"))
my_label_2.grid(column=0, row=1)

window.mainloop()

