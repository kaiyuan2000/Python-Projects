
class QuizBrain :
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def still_have_question(self):
        current_question_number = self.question_number
        total_question_number = len(self.question_list)
        if current_question_number < total_question_number:
            return True
        else:
            return False

    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q{(self.question_number + 1)} : {current_question.text} (True/ False) : ")
        if self.check_answer(user_answer, current_question.answer) :
            self.score += 1
            print("You got it right ! ")
            print(f"The correct answer was : {current_question.answer}")
            print(f"Current score is {self.score}/{(self.question_number + 1)}")
        else :
            print("You got it wrong ! ")
            print(f"The correct answer was : {current_question.answer}")
            print(f"Current score is {self.score}/{(self.question_number + 1)}")
        self.question_number += 1




