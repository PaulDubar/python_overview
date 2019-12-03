# uses question.py object class
from question import Question
# create an array of multiple choice questions
question_prompts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
# create an array of objects using the Question object class defined in question.py
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

# Now create a function that asks the user the questions and captures the answers
def run_test(questions):  # this function accepts as input the questions array
    score = 0
    for question in questions: # for each question object in the questions array do something
        answer = input(question.prompt) # store in answer the response to the question
        if answer == question.answer:
            score += 1
    print("Hey you got " + str(score) + "/" + str(len(questions)) + " right")        

# Now we need to call the run_test function to run this program
run_test(questions) # cann run_test function and pass it the questions array of objects