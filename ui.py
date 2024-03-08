from tkinter import *
from data import question_data
# THEME_COLOR = '#375362'
THEME_COLOR = '#000000'


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quiz-Game')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.canvas.create_text(100, 130, text=question_data, font=('arial', 20, 'italic'))

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)



        self.window.mainloop()
