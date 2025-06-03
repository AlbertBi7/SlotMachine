

MAX_LINES = 3
MAX_BET= 100
MIN_BET=1


def deposit():
    while (True):
        amount = input("How much would you like to deposit? $")
        if(amount.isdigit()):
            amount = int(amount)
            if(amount>0):
                break
            else:
                print("Amount should be greater than 0.")

        else:
            print("Please Enter a valid Number.")

    return amount    

def getLines():
    while (True):
        lines = input("Enter the number of lines(1-"+str(MAX_LINES)+"):")
        if(lines.isdigit()):
            lines = int(lines)
            if(1 <= lines <= MAX_LINES):
                break
            else:
                print("Please enter valid number of Lines")

        else:
            print("Please Enter a valid Number.")

    return lines 

def getBet():
    while (True):
        bet = input(f"What is amount you want to bet on each line(${MIN_BET}-${MAX_BET})? $")
        if(bet.isdigit()):
            bet = int(bet)
            if(MIN_BET <= bet <= MAX_BET):
                break
            else:
                print("Please enter valid Bet Amount")

        else:
            print("Please Enter a valid Number.")

    return bet 

def main():
    balance = deposit()
    lines = getLines()
    while True:
        bet = getBet()
        total_bet = lines * bet
        if(total_bet>balance):
            print(f"You can not bet since it exceeds your balance. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines: ${total_bet}")
    

main()