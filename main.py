from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    newq=Question(question_text,question_answer)
    question_bank.append(newq)

quiz=QuizBrain(question_bank)


while quiz.question_left():
    quiz.nextquestion()

print("\n\nYou've completed the quiz!")
print(f"Your score is: {quiz.score}/{len(quiz.qlist)}")