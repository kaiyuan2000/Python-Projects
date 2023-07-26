import data
import question_model
import quiz_brain

question_bank = []
index = (len(data.question_data))

for i in range(0,index):
    question = data.question_data[i]["text"]
    answer = data.question_data[i]["answer"]
    question_bank.append(question_model.Question(question,answer))

quiz_object = quiz_brain.QuizBrain(question_bank)

while quiz_object.still_have_question():
    quiz_object.next_question()

print("You have completed the quiz.")
print(f"Your final score was {quiz_object.score}/{quiz_object.question_number}")



