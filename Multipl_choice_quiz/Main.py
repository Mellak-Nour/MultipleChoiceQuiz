from Question import Question
           #list nrml ndir fih prompts t3 questions and the sugested answers
question_prompt=[
"Which planet in our solar system is known as the Red Planet? \nA) Earth\nB) Mars\nC) Jupiter\nD) Saturn\n",
"Which of the following authors wrote the novel: To Kill a Mockingbird?\nA) F. Scott Fitzgerald\nB) Harper Lee\nC) Jane Austen\nD) J.K. Rowling\n",
"Which river is the longest in South America?\nA) Amazon River\nB) Paraná River\nC) São Francisco River\nD) Magdalena River\n"
]
obj_list= [   #list of objects de type Question 3ndhom prompt and its answer
    Question(question_prompt[0],"B"),
    Question (question_prompt[1],"B"),
    Question(question_prompt[2],"A"),
]

def play(obj_list):
    score = 0
    for i in obj_list :
         rep = input(i.prompt)
         if rep == i.answer :
              score += 1

    print("u got score of "+str(score)+"/"+str( len(obj_list) )+" ;)")

play(obj_list)