
# * Python quiz game 


questions = (
    "What is the capital of France?",
    "What is 2 + 2?",
    "What color do you get when you mix red and white?",
    "Which planet is known as the Red Planet?"
            )
options = (
    ("A.Paris", "B.London", "C.Berlin", "D.Madrid"),
    ("A.3", "B.4", "C.5", "D.6"),
    ("A.Pink", "B.Purple", "C.Orange", "D.Green"),
    ("A.Earth", "B.Mars", "C.Jupiter", "D.Saturn")
        )

answers = ("A","B","A","B")

guesses = []
score = 0 
question_num =0 


for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT !!")
        score +=1
    else:
        print("INCORRECT!!")
        print(f"The correct answer is {answers[question_num]} ")
    question_num +=1


print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("answers: ", end= "")
for answer in answers:
    print(answer,end=" ")
print()


print("guesses: ", end= "")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions) *100)
print(f"Your score is : {score}%")