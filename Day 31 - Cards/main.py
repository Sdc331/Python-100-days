from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_SMALL = ("Ariel", 40, "italic")
FONT_BIG = ("Ariel", 60, "bold")


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

# Canvas / CARDS

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="lorem", font=FONT_SMALL)
canvas.create_text(400, 265, text="ipsum", font=FONT_BIG)
canvas.grid(row=0, column=0, columnspan=2)



# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)







window.mainloop()