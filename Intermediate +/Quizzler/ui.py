from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quizbrain : QuizBrain):

        self.quiz = quizbrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady=20, bg= THEME_COLOR)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0,row=1,columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width= 280,
                                                     text="Example",
                                                     font=("Arial", 20, "italic"),
                                                     fill="black")

        true_img = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=true_img,highlightthickness=0, command=self.click_true)
        self.trueButton.grid(column=0,row=2,pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=false_img, highlightthickness=0, command =self.click_false)
        self.falseButton.grid(column=1, row=2,pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text= f"Score :{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else :
            self.canvas.itemconfig(self.question_text, text="You have reached the end")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")

    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else :
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

