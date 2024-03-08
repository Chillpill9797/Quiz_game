from tkinter import *
from data import question_data
from main import question_func
# THEME_COLOR = '#375362'
THEME_COLOR = '#000000'

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quiz-Game')
        self.window.config(padx=50, pady=50, background=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, background="white")
        self.canvas.grid(column=0, row=0, columnspan=2)
        self.canvas.create_text(100, 130, text=question_func().question_text, font=('arial', 20, 'italic'))


        self.window.mainloop()
