import random

dice_art = {
    1: (
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"
    ),
    2: ( 
        "┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"
    ),
    3: (
        "┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"
    ),
    4: (
        "┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"
    ),
    5: (
        "┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"
    ),
    6: (
        "┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"
    )
}

dice = []

total = 0

num_of_dice  = int(input("How many dices? : "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)   # ! By this we can print all the dices in vertical position 

# ! If we want them in horizontal then 
for line in range(5): # ! here 5 represent the rows of dice (There are 5 dices)
    for die in dice:
        print(dice_art.get(die)[line],end = "")
    print()

for dic in dice:
    total += dic
    
print(f"Total is : {total}") 
