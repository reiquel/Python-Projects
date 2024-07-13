from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    # Create a list of random letters
    list_of_letters = [choice(letters) for letter in range(randint(8, 10))]
    list_of_numbers = [choice(numbers) for number in range(randint(2, 4))]
    list_of_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    # Combine the lists
    list_of_all = list_of_letters + list_of_numbers + list_of_symbols
    # Shuffle the list
    shuffle(list_of_all)
    # Convert the list to a string
    password = "".join(list_of_all)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you do not leave any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("file.txt", "a") as file:
                file.write(f"{website}| {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "carelary92@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
password_generator_button = Button(text="Generate Password", command=generate_random_password)
password_generator_button.grid(row=3, column=2, sticky="e")
add_button = Button(text="Add", width=36, command=save_info)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")



window.mainloop()
