from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []

for q in question_data:
    ques = Question(q['text'],q['answer'])
    question_list.append(ques)

quizz = QuizBrain(question_list)

while quizz.still_q():
    quizz.next_question()

print(F'Score is {quizz.score}/{len(question_list)}')