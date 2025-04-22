import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)

guesses = 0 
is_running = True 
while is_running:

    guess = input(f"Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess > highest_num  or guess < lowest_num:
            print("----------------")
            print(f"{guess} is out of range")
            print(f"Please select between {lowest_num} and {highest_num} ")
            print("----------------")
        elif guess > answer:
            print("----------------")
            print("Please go lower")
            print("----------------")
        elif guess < answer:
            print("----------------")
            print("Please go higher")
            print("----------------")
        else:
            print("----------------")
            print(f"CORRECT !! The answer was {answer}")
            print(f"The number of guesses it took is : {guesses}")
            print("----------------")
            is_running = False 
    else :
        print("----------------")
        print("invalid guess")
        print(f"Please select between {lowest_num} and {highest_num} ")
        print("----------------")
