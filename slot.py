MAX_LINES = 3


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

def get_number_of_lines():
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

def main():
    balance = deposit()
    lines=get_number_of_lines()
    

main()