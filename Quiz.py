from Question import Question
questions_prompts = [

    "What color are apples? \n(a) Red/Green \n(b) Purple \n(c) Orange"
    "What color are banannas? \n(a) Teal \n(b) Magenta \n(c) Yellow"
    "What color are strawberries? \n(a) Yellow \n(b) Red \n(c) Blue"

]
questions[
    questions(questions_prompts[0], "a")
    questions(questions_prompts[1], "c")
    questions(questions_prompts[2], "b")
]

def runtest(questions):
    score = 0
    for question in questoins:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")