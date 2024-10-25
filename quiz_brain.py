class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_q(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        curr_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q {self.question_number} {curr_q.text} T/F ")
        self.check_answer(user_answer,curr_q.answer)
    
    def check_answer(self,user_answer,curr_answer):
        if user_answer == curr_answer:
            print('You got it right')
            self.score += 1
        else:
            print('You got it wrong')