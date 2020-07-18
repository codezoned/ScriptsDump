import random
import sys

print "Welcome to Tic Tac Toe!"
print "The board is set up like this: "
print "0|1|2"
print "3|4|5"
print "6|7|8"
print "Enter your first move, 0 through 8. (You are O's, the AI is X's)"

# The 'pairs' list is used to check and see if anyone has won the game.
# -------|           Verticals          |          Horizontals           |      Diagonals      |
pairs = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])

# 'Corners' is used for the AI to let it pick random corners.
corners = [0, 2, 6, 8]
board = ["_", "_", "_", "_", "_", "_", " ", " ", " "]

# 'Turn' keeps track of whose turn it is. During the game it is either "AI" or "PLAYER".
turn = "PLAYER"

# 'Aiturn' lets the AI know how many turns it has taken.
aiturn = 0


# Just prints the board and starts the next turn
def printboard(turn, board, aiturn):
    print board[0] + "|" + board[1] + "|" + board[2]
    print board[3] + "|" + board[4] + "|" + board[5]
    print board[6] + "|" + board[7] + "|" + board[8]
    print "Turn: " + str(turn)
    if turn == 0:
        playermove(turn, board, aiturn)
    if turn == "AI":
        aiturn += 1
        aimove(turn, board, aiturn, corners)
    if turn == "PLAYER":
        playermove(turn, board, aiturn)


# Prompts the player to move
# I added some stuff that makes sure the input is legit. Thanks to Github user Kaligule for opening an issue.
def playermove(turn, board, aiturn):
    choice = raw_input("Enter a number 0-8: ")
    if choice.isdigit() == False:
        print "Keep it an integer, buddy."
        playermove(turn, board, aiturn)
    if int(choice) > 8 or int(choice) < 0:
        print "Make that a number between 0 and 8."
        playermove(turn, board, aiturn)
    if board[int(choice)] == 'X' or board[int(choice)] == 'O':
        print "That's already taken! Try again."
        playermove(turn, board, aiturn)
    else:
        board[int(choice)] = "O"
    turn = "AI"
    checkforwin(turn, board, aiturn)


# Makes the AI move.
def aimove(turn, board, aiturn, corners):
    alreadymoved = False
    completes = ([0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6])

    # Pretty self-explanatory, just chooses a random empty corner.
    def cornerchoice(corners, board, alreadymoved):
        goodchoices = []
        if not alreadymoved:
            for i in corners:
                if board[i] == " " or board[i] == "_":
                    goodchoices.append(i)
            board[random.choice(goodchoices)] = "X"

    # If the player didn't take the center on their first move, this makes the AI take the center.
    if aiturn == 1:
        if board[4] != "O":
            board[4] = "X"
            alreadymoved = True
        else:
            cornerchoice(corners, board, alreadymoved)
            alreadymoved = True

    # Checks to see if there are any possible ways for the game to end next turn, and takes proper action.
    else:
        for x in completes:
            # Offensive
            if board[x[0]] == "X" and board[x[1]] == "X" and board[x[2]] != "O":
                board[x[2]] = "X"
                alreadymoved = True
                break
            if board[x[1]] == "X" and board[x[2]] == "X" and board[x[0]] != "O":
                board[x[0]] = "X"
                alreadymoved = True
                break
            if board[x[0]] == "X" and board[x[2]] == "X" and board[x[1]] != "O":
                board[x[1]] = "X"
                alreadymoved = True
                break
    # Tweaked it here a little bit, thanks to reddit user mdond for letting me know. It defending items closer to the
    # start of the list 'pairs' before it would play offensive with items later in 'pairs'.
        for x in completes:
            if alreadymoved == False:
                # Defensive
                if board[x[0]] == "O" and board[x[1]] == "O" and board[x[2]] != "X":
                    board[x[2]] = "X"
                    alreadymoved = True
                    break
                if board[x[1]] == "O" and board[x[2]] == "O" and board[x[0]] != "X":
                    board[x[0]] = "X"
                    alreadymoved = True
                    break
                if board[x[0]] == "O" and board[x[2]] == "O" and board[x[1]] != "X":
                    board[x[1]] = "X"
                    alreadymoved = True
                    break

    # If none of the above has worked and it isn't during the first few turns, it chooses a random 'side' space to
    # fill (this rarely happens). If it is during the AI's 2nd turn, it chooses a corner piece because of this flaw:
    # Turn 1
    # _|_|_
    # _|O|_
    # X| |
    #
    # Turn 2
    # _|_|O
    # _|O|X <--- Random side piece
    # X| |
    #
    # Turn 3
    # O|!|O The two exclamation points represent where an O could be placed to win, but if the AI chooses a corner
    # _|O|X in turn 2, this could be prevented.
    # X| |!
    #
    # Also, the code below avoids situations where the player is able to have two possible winning moves next turn.
    # For example:
    #
    # O|_|X <--- Random corner choice
    # _|X|_  If the AI were to choose a corner, the player could win.
    # O| |O
    #
    # But when the AI chooses a side piece the below happens.
    #
    # O|_|_
    # ?|X|X This forces the player to place an O at the square with the '?', so the two possible solutions don't occur
    #  | |O
    #

    if not alreadymoved:
        # The 'and board[4] == "O"' part was added because of another exploit similar to the last one mentioned above
        if aiturn == 2 and board[4] == "O":
            cornerchoice(corners, board, alreadymoved)
        else:
            sides = [1, 3, 5, 7]
            humansides = 0
            for i in sides:
                if board[i] == "O":
                    humansides += 1
            if humansides >= 1:
                cornerchoice(corners, board, alreadymoved)
            else:

                goodchoices = []
                for i in sides:
                    if board[i] == " " or board[i] == "_":
                        goodchoices.append(i)
                if goodchoices == []:
                    cornerchoice(corners, board, alreadymoved)
                else:
                    board[random.choice(goodchoices)] = "X"

    turn = "PLAYER"
    checkforwin(turn, board, aiturn)


def checkforwin(turn, board, aiturn):
    for x in pairs:
        zero = board[x[0]]
        one = board[x[1]]
        two = board[x[2]]
        if zero == one and one == two:
            if zero == "X":
                print "AI wins."
                end()
            if zero == "O":
                print "Human wins. Did you cheat?"
                end()
        else:
            filledspaces = 0
            for i in range(8):
                if board[i] != " " and board[i] != "_":
                    filledspaces += 1
                if filledspaces == 8:
                    print "A draw! You will never win!"
                    end()

    printboard(turn, board, aiturn)

# Displays the final board #

def end():
    print "Here is the final board."
    print board[0] + "|" + board[1] + "|" + board[2]
    print board[3] + "|" + board[4] + "|" + board[5]
    print board[6] + "|" + board[7] + "|" + board[8]
    sys.exit(0)


printboard(turn, board, aiturn)
