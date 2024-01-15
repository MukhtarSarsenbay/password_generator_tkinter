from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

# for char in range(nr_letters):
#   password_list.append(random.choice(letters))

# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title="website", message =f"These are the details are entered:\n Email:{email}\nPassword:{password} \n Is okay to save them or not?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
#labels
label = Label(text="Website:")
label.grid(row=1, column=0)
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = Label(text="Password")
label3.grid(row=3, column=0)

#Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "mukhtar.sarsenbay@nu.edu.kz")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Button
button_generate = Button(text="Generate Password",command=generate)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=36,command=save)
button_add.grid(row=4, column=1, columnspan=2)





window.mainloop()