from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showerror(title="Oops!", message="Website name cannot be empty."
                                                    " Kindly fill again.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                website_password = data[website]

        except FileNotFoundError:
            messagebox.showerror(title="File Not Found",
                                 message="No data file found.\nKindly add at least one entry in the program to search "
                                         "through the passwords.")

        except KeyError:
            messagebox.showerror(title=website,
                                 message="No data for the website exists.")
        else:
            messagebox.showinfo(title=website, message=f"Email: {website_password['username']}\n"
                                                       f"Password: {website_password['password']}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    website = website_entry.get()
    username = id_entry.get()
    password = password_entry.get()

    data_dict = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Field(s) cannot be empty."
                                                    " Kindly fill again.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(data_dict, data_file, indent=4)

        else:

            data.update(data_dict)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas()
canvas.config(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:", pady=5)
website_label.grid(column=0, row=1)

id_label = Label()
id_label.config(text="Username/Email:", pady=5)
id_label.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:", pady=5)
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW", padx=(0, 10))
website_entry.focus()

id_entry = Entry()
id_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
id_entry.insert(0, "guptahriday4444@gmail.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW", padx=(0, 10), pady=5)

search_button = Button()
search_button.config(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

generate_password_button = Button()
generate_password_button.config(text="Generate Password", command=generate_password, width=15)
generate_password_button.grid(column=2, row=3)

add_button = Button()
add_button.config(text="Add", command=add_details)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
