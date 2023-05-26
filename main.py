from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]


    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    newdata = {
        website: {
            "username" : username,
            "password": password,
        }
    }

    if (len(website) == 0 or len(password)==0):
        messagebox.showinfo(title="Fill all entries", message="Please fill all empty boxes")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:


            with open("data.json", "w") as file:
                json.dump(newdata,file,indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)

LOGO =PhotoImage(file="logo.png")
canvas.create_image(100,100,image=LOGO)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2,sticky="W")

username_label = Label(text="Email/Username:")
username_label.grid(column=0,row=2)

username_entry = Entry(width=35)
username_entry.grid(column=1,row=2,columnspan=2,sticky="W")
username_entry.insert(0, "manohar.yekkala@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3,sticky="W")

gen_password = Button(text="Generate Password",borderwidth=1,command=gen_pass)
gen_password.grid(column=2,row=3,sticky="W")

add_button = Button(text="Add",width=36,borderwidth=1,command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky="W")




window.mainloop()
