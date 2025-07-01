from tkinter import *
import pandas
import random
import threading

BACKGROUND_COLOR = "#B1DDC6"
FONT_SMALL = ("Ariel", 40, "italic")
FONT_BIG = ("Ariel", 60, "bold")
FRENCH_COLOR = "black"
ENGLISH_COLOR = "white"



window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

def update_db():
    global temp
    try:
        temp = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
        list(temp)
        temp.remove(entry)
    except FileNotFoundError:
        temp = data
        list(temp)
        temp.remove(entry)
    except NameError:
        pass
    else:
        pandas.DataFrame(temp).to_csv("data/words_to_learn.csv", index=False)

def english_card():
    canvas.itemconfig(current_card, image=card_back)
    canvas.itemconfig(title, text="English", fill=ENGLISH_COLOR)
    canvas.itemconfig(word, text=entry['English'], fill=ENGLISH_COLOR)

def next_card():
    global entry
    timer = threading.Timer(3.0, english_card)
    update_db()
    try:
        entry = random.choice(temp)
    except:
        entry = random.choice(data)
    canvas.itemconfig(current_card, image=card_front)
    canvas.itemconfig(title, text="French", fill=FRENCH_COLOR)
    canvas.itemconfig(word, text=entry['French'], fill=FRENCH_COLOR)
    timer.start()



# Images
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

# Canvas / CARDS

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
current_card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="lorem", font=FONT_SMALL)
word = canvas.create_text(400, 265, text="ipsum", font=FONT_BIG)
canvas.grid(row=0, column=0, columnspan=2)



# Buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, border=0)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_img, highlightthickness=0, border=0, command=next_card)
right_button.grid(row=1, column=1)







window.mainloop()