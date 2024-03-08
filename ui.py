from tkinter import *
from quiz_brain import QuizBrain
# THEME_COLOR = '#375362'
THEME_COLOR = '#000000'


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_data = quiz_brain
        self.window = Tk()
        self.window.title('Quiz-Game')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="", width=280, font=('arial', 20, 'italic'))

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz_data.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
