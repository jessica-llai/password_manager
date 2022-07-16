from tkinter import *  # only include classes
from tkinter import Tk
from tkinter import messagebox  # not a class, have to import seperately
import random
import pyperclip

FONT = ("Arial", 15, "normal")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)
    entry_password.insert(0, password)  # after generating, show it in the entry box
    pyperclip.copy(password)  # copy the new password in the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    if len(website) ==0 or len(password) == 0:
        messagebox.showwarning(title="warning", message="please enter correct information")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Set the username: {username}, "
                                                      f"and new password: {password} for the website {website}, is it OK?")
        # is_ok return true/false
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f"{website} | {username} | {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

canvas = Canvas(window, width=200, height=200, highlightthickness=0)
my_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

# label
label_website = Label(text="Website:", font=FONT)
label_website.grid(column=0, row=1)

label_username = Label(text="Username/Email:", font=FONT)
label_username.grid(column=0, row=3)

label_password = Label(text="Password:", font=FONT)
label_password.grid(column=0, row=5)

# entry
entry_website = Entry(width=35)  #can change the width together with column span
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()  # put the cursor in the entry box


entry_username = Entry(width=35)
entry_username.grid(column=1, row=3, columnspan=2)
entry_username.insert(0, "laiy20010413@gmail.com")

entry_password = Entry(width=19)
entry_password.grid(column=1, row=5)


# button
button_password = Button(text="Generate Password", font=FONT, width=15, command=gen_password)
button_password.grid(column=2, row=5)

button_add = Button(text="Add", font=FONT, width=36, command=add)
button_add.grid(column=1, row=6, columnspan=2)















window.mainloop()