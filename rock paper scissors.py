import random

options = ("rock","paper","scissors")
score_player = 0
score_computer = 0
running = True


print("---------------------------------------------")        
while running:
    computer = random.choice(options)
    player = input("Enter a choice(rock,paper,scissors) : ").lower()
    while player not in options:
        print("Please choose one of the three options only!!")
        player = input("Enter a choice(rock,paper,scissors) : ").lower()
    
    print(f"Player : {player}")
    print(f"computer : {computer}")
        
    if player == computer:
        print("It's a tie🗿!!")
        print("You and computer both will get point")
        score_player += 1
        score_computer += 1

    elif player == "rock" and computer == "scissors":
        print("You won 😊!!")
        print("You will get one point")
        score_player += 1

    elif player == "scissors" and computer == "paper":
        print("You won 😊!!")
        print("You will get one point")
        score_player += 1

    elif player == "paper" and computer == "rock":
        print("You won 😊!!")
        print("You will get one point")
        score_player += 1
    else:
        print("You Lost 😒!!")
        print("Computer will get one point")
        score_computer += 1


    if not (input ("Play again ? (y/n) : ").lower()) == "y":
        running = False
        

    print("---------------------------------------------")    
    
    

print("\n \n --------The final score--------")
print(f"Your score : {score_player}")
print(f"Computer score : {score_computer}")
print("-------------------------------")


