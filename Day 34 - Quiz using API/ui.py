from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 13, "normal"))
        self.label.grid(row = 0, column = 1)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row = 1, column = 0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="TESTTESTTEST", font=FONT, fill=THEME_COLOR, width=280)
        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        self.rightbutton = Button(image=right_image, bg=THEME_COLOR, highlightthickness=0)
        self.rightbutton.grid(row = 2, column = 0)
        self.wrongbutton = Button(image=wrong_image, bg=THEME_COLOR, highlightthickness=0)
        self.wrongbutton.grid(row = 2, column = 1)
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)