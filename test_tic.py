

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def displayInstructions():
    print(""" This is a game of Tic-Tac-Toe. You will select an empty location
and enter its index to select a move. The first player will be X
and the second will be O.  \n """)

def getMove(board):
    print('[' + board['1'] + ']' + '[' + board['2'] + ']' + '[' + board['3'] + ']')
    print('[' + board['4'] + ']' + '[' + board['5'] + ']' + '[' + board['6'] + ']')
    print('[' + board['7'] + ']' + '[' + board['8'] + ']' + '[' + board['9'] + ']')


def main():
    displayInstructions()

    turn = 'X'
    count = 1


    for i in range(10):
        getMove(theBoard)
        print(turn + ', ' "what is your move?")

        move = input()

        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

     
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                getMove(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                getMove(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                getMove(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                getMove(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                getMove(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                getMove(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                getMove(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                getMove(theBoard)
                print("\nGame Over.\n")                
                print(turn + " won.")
                break 

        
        if count == 10:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    
    reset = input("Do want to play another game?(y/n)")
    if reset == "y" or reset == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        main()

if __name__ == "__main__":
    main()
