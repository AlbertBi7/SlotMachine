import random

MAX_LINES = 3
MAX_BET= 100
MIN_BET=1

ROWS = 3
COLS = 3

symbolCount = {
    'A':2,
    'B':4,
    'C':6,
    'D':8
}

def getSlotSpin(rows,cols,symbols):
    allSymbols=[]
    for symbol , symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    column = []

    for i in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for j in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        column.append(column)

    return column

def printSlot (columns):
    for i in range(len(columns[0])):
        for j, column in columns:
            if( i!=len(columns)-1):
                print(columns[i], "|")
            else:
                print(column[i])





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
    

