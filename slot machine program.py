
# * Slot machine program
import random

def spin_row():
    symbols = ['🍒','🍉','🍋', '🔔','⭐']
    # ! results = [random.choice(symbols) for x in range 3 ]
    # ! return results
    
    # ! instead we can do is
    return [random.choice(symbols) for x in range(3)]
def print_row(row):
    print("************************")
    print(" | ".join(row))
    print("************************")

def get_payout(row,bet):
    
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet *100
    return 0
def main():
    balance = 0
    print("************************")
    print("Welcome to python slots")
    print("Symbols : 🍒 🍉 🍋 🔔 ⭐")
    print("************************")
    
    if balance <= 0:
        if input("Do you want to add balance in your account (Y/N) : ").strip().upper() != 'Y':
            return 0
        else:
            attempts = 5
            for i in range(attempts):
                add = int(input("Enter the amount you want to add in the account : "))
            
              
                if add <= 0:
                    print("Please enter a valid amount")
                    if i == attempts - 1 :
                        print("This is your last chance, otherwise the program will shut down")
                        add = int(input("Enter the amount you want to add in the account : "))
                if add > 0:
                    balance += add
                    print(f"Amount successfully added! New balance = ${balance}")
                    break   

            else:
                print("Too many invalid input!! Shutting down the program")
                return 0        
    while (balance > 0):
        print(f"Current balance : ${balance}")
        
        bet = input("Place your bet amount : ")
        
        if not bet.isdigit():
            print("Please enter a valid number ")
            continue
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("Bets must be greater than 0")
            continue
        
        balance -= bet 
        
    
        row = spin_row()
        print("spinning... \n")
        print_row(row)
        
        
        payout = get_payout(row,bet)
        
        if payout > 0 :
            balance += payout 
            print(f"You won ${payout}")
        else:
            print(f"Sorry you lost this round")
            
        
        play_again = input("\nDo you want to spin again(Y/N): ").upper()
        
        if  play_again != 'Y':
            break

    print("************************")
    print(f"Game over !! Your final balance is {balance}")
    print("************************")

if __name__ == '__main__':
    main()