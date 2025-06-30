from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def send_data():
    web = web_input.get()
    user = username_input.get()
    cred = pass_input.get()
    print(web)
    with open("data.txt", "a") as f:
        if not web or not user or not cred:
            print("You need to provide all the inputs")
        else:
            f.write(f"{web} | {user} | {cred} \n")


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

web_input = Entry(width=52)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()
username_input = Entry(width=52)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "esdecek@gmail.com")
pass_input = Entry(width=33)
pass_input.grid(row=3, column=1)

gen_button = Button(text="Generate Password")
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(command=send_data)


window.mainloop()