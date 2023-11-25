from random import randint

#interface creation initialized to zero
global plates 
global symbol
plates = [
          '-', '-', '-',
          '-', '-', '-',
          '-', '-', '-'
         ]

#printing the plates

def printBoard(plates):
    print("  " + "1" + " | " + '2' + " | " + '3')
    print("  " + plates[0] + " | " + plates[1] + " | " + plates[2])
    print("-------------")
    print("  " + "4" + " | " + '5' + " | " + '6')
    print("  " + plates[3] + " | " + plates[4] + " | " + plates[5])
    print("-------------")
    print("  " + "7" + " | " + '8' + " | " + '9')
    print("  " + plates[6] + " | " + plates[7] + " | " + plates[8])

#play in one user
def userPlay(plates, symbol):
    while True:
        try:
            selectionNum = int(input("Please enter a number from 1 to 9: "))
            if 1 <= selectionNum <= 9 and plates[selectionNum - 1] == '-':
                plates[selectionNum - 1] = symbol
                break
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#computer player

def computerPlay(plates, symbol):
    try:
        computerSelection = randint(0, 8)
        if plates[computerSelection] == '-':
            plates[computerSelection] = symbol
        else:
            computerPlay(plates, symbol)
    except Exception:
            print("Something went wrong")

#checking winning (3ways)
def chechWiningHoriozntal(plates, symbol):
    if (plates[0] == plates[1] == plates[2] == symbol or
        plates[3] == plates[4] == plates[5] == symbol or 
        plates[6] == plates[7] == plates[8] == symbol):
        return (1)
    return (0)
def checkWiningVertical(plates, symbol):
    if (plates[0] == plates[3] == plates[6] == symbol or
        plates[1] == plates[4] == plates[7] == symbol or 
        plates[2] == plates[5] == plates[8] == symbol):
        return (2)
    return (0)
def checkWiningDiagonal(plates, symbol):
    if (plates[0] == plates[4] == plates[8] == symbol or
        plates[2] == plates[4] == plates[6] == symbol):
        return (3)
    return (0)

#main function for checking winning
def checkWining(plates, symbol):
    if (chechWiningHoriozntal(plates, symbol)):
        return (1)
    if (checkWiningVertical(plates, symbol)):
        return (2)
    if (checkWiningDiagonal(plates, symbol)):
        return (3)

    return (0)

#switch players
def switchPlayers(symbol):
    if (symbol == 'X'):
        symbol = 'O'
    else:
        symbol = 'X'
    return symbol

#wining display function
def wining(plates, symbol):
    printBoard(plates)
    if (checkWining(plates, symbol) == 1):
        print("\n" + symbol + " Won by a horizontal play!!!!!")
    elif (checkWining(plates, symbol) == 2):
        print("\n" + symbol + " Won by a vertical play!!!!!")
    elif (checkWining(plates, symbol) == 3):
        print("\n" + symbol + " Won by a diagonal play!!!!!")
    
#checking tie function
def checkTie(plates):
    for i in range(len(plates)):
        if plates[i] == '-':
            return False
    print("The game ended in a tie, tough one!!")
    return (True)

#reseting game function
def resetGame(plates):
    for i in range(len(plates)):
        plates[i] = '-'

#asking for a another round
def playAgainQuestion(plates):
    while True:
        answer = input("Do you want to play again(Y/N)??")
        if (answer == 'Y' or answer == 'y'):
            resetGame(plates)
            break
        elif (answer == 'N' or answer == 'n'):
            print("Thank you for playing in our game!!!")
            exit()
        else:
            print("Wrong input!!!, enter correct input")
            continue
def PVP(plates, symbol):
        while True:
            if checkTie(plates):
                playAgainQuestion(plates)
            printBoard(plates)
            userPlay(plates, symbol)
            if checkWining(plates, symbol):
                wining(plates, symbol)
                playAgainQuestion(plates)

            symbol = switchPlayers(symbol)
            
def PvComputer(plates, symbol):
        while True:
            if checkTie(plates):
                playAgainQuestion(plates)
            printBoard(plates)
            symbol = switchPlayers(symbol)
            userPlay(plates, symbol)
            if checkWining(plates, symbol):
                wining(plates, symbol)
                playAgainQuestion(plates)
            symbol = switchPlayers(symbol)
            computerPlay(plates, symbol)
            if checkWining(plates, symbol):
                wining(plates, symbol)
                playAgainQuestion(plates)
            
#main function                
def main():
    plates = ['-'] * 9
    symbol = 'X'
    gameMode = int(input("Select the mode you want to play 1-player or 2-players(1/2): "))
    if (gameMode == 1):
        PvComputer(plates, symbol)
    if (gameMode == 2):
        PVP(plates, symbol)
        
main()
