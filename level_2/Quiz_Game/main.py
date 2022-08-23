from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for questions in question_data:
    question = questions["question"]
    correct_answer = questions["correct_answer"]
    new_question = Question(question, correct_answer)
    question_bank.append(new_question)

quiz = Quiz(question_bank)

quiz.still_questions_left()

