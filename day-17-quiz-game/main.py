from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question = Question(i["question"], i["correct_answer"])
    question_bank.append(question)

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    brain.next_question()

print("YOU HAVE COMPLETED THE QUIZ!")
print(f"Your final score is: {brain.score}/{len(brain.question_list)}")

