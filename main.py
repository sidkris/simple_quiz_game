from data import question_data
from model import Question
from engine import Engine

question_bank = []

for i in question_data:
    _question = i["text"]
    _answer = i["answer"]
    new_question = Question(_question, _answer)
    question_bank.append(new_question)
    
quiz = Engine(question_bank)

while quiz.more_questions:
  quiz.next_question()

print("You have comepleted the quiz.")
print("Your total score is {} out of {}".format(quiz.scoe, quiz.question_number))
print("Thanks for playing!")