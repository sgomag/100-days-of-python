from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

COLUMN_0_WIDTH = 20
COLUMN_1_WIDTH = 10
COLUMN_2_WIDTH = 20
PADDING = {"padx": 1, "pady": 1, "sticky": "we"}
STANDARD_USERNAME = "sgomag@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0,password)
    # Automatically copy password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_input.get().strip()
    username = username_input.get().strip()
    password = password_input.get().strip()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
     }
    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please fill all fields.")
    else:
        try: # If file already exists
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError: # If file doesn't exit
            data = new_data
        else:
            # updating old data with new data
            data.update(new_data)
        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)

        # Reset fields
        website_input.delete(0, END)
        username_input.delete(0, END)
        username_input.insert(0, STANDARD_USERNAME)
        password_input.delete(0, END)
        website_input.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get().strip()
    if website == "":
        pass
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title=f"Error", message="No data file found")
        else:
            if website in data:
                messagebox.showinfo(title=website,
                                    message=f"username: {data[website]["username"]}\n"
                                            f"password: {data[website]["password"]}")
            else:
                messagebox.showerror(title=f"Error", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx= 50, pady=50)

# Canvas ------- #
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(130,100,image=logo_img)
canvas.grid(column=1, row=0)

# Labels ------- #
website_label = Label(text= "Website:", anchor = "e")
website_label.grid(column=0, row=1, **PADDING)

username_label = Label(text= "Email/Username:", anchor = "e")
username_label.grid(column=0, row=2, **PADDING)

password_label = Label(text= "Password:", anchor="e")
password_label.grid(column=0, row=3, **PADDING)

# Inputs ------- #
website_input = Entry(width=COLUMN_1_WIDTH)
website_input.grid(column=1, row=1, **PADDING)
website_input.focus()

username_input = Entry(width=COLUMN_1_WIDTH + COLUMN_2_WIDTH)
username_input.grid(column=1, row=2, columnspan=2, **PADDING)
username_input.insert(0, STANDARD_USERNAME)

password_input = Entry(width=COLUMN_1_WIDTH)
password_input.grid(column=1, row=3, **PADDING)

# Buttons ------- #
generate_button = Button(text="Generate password", width=COLUMN_2_WIDTH, command=generate_password)
generate_button.grid(column=2, row=3, **PADDING)

add_button = Button(text="Add", width=COLUMN_1_WIDTH + COLUMN_2_WIDTH, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, **PADDING)

search_button = Button(text="Search", width=COLUMN_2_WIDTH, command=find_password)
search_button.grid(column=2, row=1, **PADDING)

window.mainloop()