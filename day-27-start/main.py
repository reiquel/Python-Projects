# This is a sample Python script.
from  tkinter import *
#
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


# my_label = Label(text="I am a label", font=("Arial", 25))
# my_label.pack()
# input = Entry(width=10)
# input.pack()
# def change_label():
#     new_text = input.get()
#     my_label.config(text=new_text )
#
# button = Button(text="Click me", command=change_label)
# button.pack()

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


my_label = Label(text="I Am a Label", font=("Arial", 15, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)

button = Button(text="New Button", command=button_clicked)
button.grid(column=1, row=1)

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)







window. mainloop()

# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# number_added = add(5, 20, 80, 90, 100, 58, 45, 60, 27, 78, 12, 35)
# print(number_added)
#
#
# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)