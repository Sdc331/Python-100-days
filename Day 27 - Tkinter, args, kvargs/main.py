import tkinter

window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(230, 120)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="is equal to")
my_label.grid(row=1, column=0)

ml_label = tkinter.Label(text="Miles")
ml_label.grid(row=0, column=2)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

result = tkinter.Label(text=0)
result.grid(row=1, column=1)

def click():
    result.config(text=float(input.get()) * 1.609344)
my_button = tkinter.Button()
my_button.config(text="Calculate", command=click)
my_button.grid(row=2, column=1)

input = tkinter.Entry(width=10)
input
input.grid(row=0, column=1)


########## v MUST BE THE LAST THING v ###############
window.mainloop() 