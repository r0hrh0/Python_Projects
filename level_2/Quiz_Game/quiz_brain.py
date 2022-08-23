class Quiz:

    def __init__(self, question_bank):
        self.question_list = question_bank
        self.question_number = 0
        self.score = 0

    def still_questions_left(self):
        while self.question_number < len(self.question_list):
            self.ask_question()

        self.final_score()

    def ask_question(self):
        new_question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].correct_answer
        self.question_number += 1
        choice = input(f"Q{self.question_number}. {new_question} (True/False)? ").lower()
        self.check_answer(choice, correct_answer)

    def check_answer(self, choice, correct_answer):
        if choice == correct_answer.lower():
            self.score += 1
            print(f"Correct Answer!")
        else:
            print(f"Wrong Answer.")
        print(f"Current Score: {self.score}/{len(self.question_list)}")

    def final_score(self):
        print(f"\n Your final score is {self.score}/{self.question_number}")
