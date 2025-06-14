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

symbolValue = {
    'A':5,
    'B':4,
    'C':3,
    'D':2
}

def getWinnings(columns, lines, bet, values):
    winning = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol !=symbolToCheck:
                  break
        else:
            winning += values[symbol] * bet
            winningLines.append(line+1)

    return winning, winningLines
          



def getSlotSpin(rows,cols,symbols):
    allSymbols=[]
    for symbol , symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns = []

    for i in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for j in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def printSlot (columns):
    for i in range(len(columns[0])):
        for j, column in enumerate(columns):
            if( j!=len(columns)-1):
                print(column[i], end = " | ")
            else:
                print(column[i], end = " ")

        print()




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

def spin(balance):
    lines = getLines()
    while True:
        bet = getBet()
        total_bet = lines * bet
        if(total_bet>balance):
            print(f"You can not bet since it exceeds your balance. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines: ${total_bet}")

    slots = getSlotSpin(ROWS,COLS,symbolCount)
    printSlot(slots)
    winnings ,winningLine = getWinnings(slots, lines, bet, symbolValue )
    print(f"Your winnings are {winnings}")
    print(f"You won on line:" ,*winningLine)

    return winnings - bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        choice = input("Press Enter to play (q to quit)")
        if choice == 'q':
            break
        balance += spin(balance)
    print(f"You have left with ${balance}")

main()