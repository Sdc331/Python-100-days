from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=30, bg="white")

# LOGO 
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website = Label(text="Website:", bg="white")
website.grid(row=1, column=0)
username = Label(text="Email/Username:", bg="white")
username.grid(row=2, column=0)
password = Label(text="Password:", bg="white")
password.grid(row=3, column=0)

web_input = Entry(width=48)
web_input.grid(row=1, column=1, columnspan=2)
username_input = Entry(width=48)
username_input.grid(row=2, column=1, columnspan=2)
pass_input = Entry(width=30)
pass_input.grid(row=3, column=1)

gen_button = Button(text="Generate Password")
gen_button.grid(row=3, column=2)
add_button = Button(text="Add")
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()