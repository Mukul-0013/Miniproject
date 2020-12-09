''' Miniproject Code on Tic-Tac-Toe '''

theBoard = {'1': '.' , '2': '.' , '3': '.' ,
            '4': '.' , '5': '.' , '6': '.' ,
            '7': '.' , '8': '.' , '9': '.' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['1'] + ' ' + board['2'] + ' ' + board['3'])
    print(board['4'] + ' ' + board['5'] + ' ' + board['6'])
    print(board['7'] + ' ' + board['8'] + ' ' + board['9'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    count = 0
    print("Enter a name for the X player:")
    x=input()
    print("Enter a name for the O player:")
    o=input()

    f=1

    while f==1:
          print("Who plays first, "+ x +" or " + o + " ?")
          turn=input()
          if turn==x or turn==o:
              f=0
          else:
              print(turn + " is not a registered player.")

    print("Board: (Row , Column)\n(0,0) (0,1) (0,2)\n(1,0) (1,1) (1,2)\n(2,0) (2,1) (2,2)\n")

    for i in range(10):
        printBoard(theBoard)
        print("Player of current turn: " + turn)

        if turn==x:
            a='X'
        else:
            a='O'

        f=0
        while f==0:
           print("Choose a row number (0 to 2):")
           r=input()
           if r=='0' or r=='1' or r=='2':
               print("Choose a column number (0 to 2):")
               c=input()
               if c=='0' or c=='1' or c=='2':
                   f=1
               else:
                   print( c + " is not a valid column.")
           else:
               print(r + " is not a valid row.")
           if f==1:
               z=(int(r)*3)+int(c)+1
               move=str(z)

               if theBoard[move] == '.':
                   theBoard[move] = a
                   count += 1
               else:
                   print("That place is already filled.\nMove to which place?")
                   f=0
                   continue


        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != '.':  # across the bottom
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != '.': # across the middle
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != '.':# across the top
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != '.': # vertically the left side
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != '.': # vertically the middle
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != '.': # vertically the right side
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != '.': # diagonal
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != '.': # diagonal
                printBoard(theBoard)
                print("\nGame is over:")
                print(turn + " wins!")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame is over.")
            print("It's a Tie!")
            break

        # Now we have to change the player after every move.
        if turn == x:
            turn = o
        else:
            turn = x

    # Now we will ask if player wants to restart the game or not.
    e=0
    while e==0:
        restart = input("Would you like to play again? (y/n)")
        if restart == "y" or restart == "Y":
            for key in board_keys:
                theBoard[key] = "."
            e=1
            game()
        elif restart!="n" and restart!="N":
            print("Invalid entry")
        elif restart=="n" or restart=="N":
            break




if __name__ == "__main__":
    game()
