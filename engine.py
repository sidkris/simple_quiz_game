class Engine:
  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0

  def more_questions(self):
    return self.question_number < len(self.question_list)
    
  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_input = input("Q.{} : {} (True/False) : ".format(self.question_number, current_question.text))
    self.check_answer(user_input, current_question.answer)

  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print("Correct answer! Well done.")
      self.score += 1
      print("Your current score is : {} out of {}\n".format(self.score, self.question_number))
    else:
      print("That's the wrong answer. The correct answer is -- {}".format(correct_answer))
      print("Your current score is : {} out of {}\n".format(self.score, self.question_number))


