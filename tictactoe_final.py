import os
import random

def print_menu():
    print('***********************')
    print("Welcome to Tic Tac Toe!")
    print('***********************')
    print("Two player game:   1")
    print("Play vs computer:  2")
    print("Instructions:      3")
    print("Exit Game:         4")
    print('***********************')

def show_board(board):
    print("-------------")
    print("|",  board[7],  "|",  board[8],  "|",  board[9],  "|")
    print("-------------")
    print("|",  board[4],  "|",  board[5],  "|",  board[6],  "|")
    print("-------------")
    print("|",  board[1],  "|",  board[2],  "|",  board[3],  "|")
    print("-------------")

def sample_board():
    print("-----------")
    print(" 7 "," 8 "," 9 ")
    print("-----------")
    print(" 4 "," 5 "," 6 ")
    print("-----------")
    print(" 1 "," 2 "," 3 ")
    print("-----------")

def check_win(board1, let):
       #checks the three rows for the same letter
    return ((board1[1] == let and board1[2] == let and board1[3] == let) or
       (board1[4] == let and board1[5] == let and board1[6] == let) or
       (board1[7] == let and board1[8] == let and board1[9] == let) or
       #checks the three columns for the same letter
       (board1[1] == let and board1[4] == let and board1[7] == let) or
       (board1[2] == let and board1[5] == let and board1[8] == let) or
       (board1[3] == let and board1[6] == let and board1[9] == let) or
       #checks the two diagonals for the same letter
       (board1[1] == let and board1[5] == let and board1[9] == let) or
       (board1[3] == let and board1[5] == let and board1[7] == let))

def new_game():
    while True:
        choice = input("Do you want to play again? (y/n) ")
        if choice == "y":
           return True
        if choice == "n":
           return False
        else:
           print("Not a valid choice! please choose between y or n")
    

def get_input():
    valid = False
    while not valid:
	    try:
		    move = input("Where would you like to place (1-9)? ")
		    move = int(move)
		    if (move >= 1 and move <= 9) and (board[move] == " " ):
			    return move
		    else:
			    print ("That is not a valid move! Please try again.\n")
	    except Exception as e:
			    print (move + " is not a valid move! Please try again.\n")

def print_instruction(): 
    print("\n")
    print("Please use the following numbers to make your move")
    print("The first player to reach three X's or O's wins!")
    sample_board()

def random_move(board, moves):
    #checks for a free spot, chooses one random 
    possible_moves = []
    for i in moves:
        if board[i] == " " :
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def clone_board(board):
    #creates a duplicate of the board for the AI
    clone = []
    for i in board:
        clone.append(i)
    return clone

def print_dog():
    #a little ascii art for fun :)
    print("")
    print("     ,                    ,' e`--o")
    print("    ((                   (  | __,'")
    print("     \\~----------------' \_;/")
    print("     (  A TACS.CO. GAME     /")
    print("     /) ._______________.  )")
    print("    (( (               (( (")
    print("     ``-'               ``-'")
    print("")

def computer_move(board, comp_letter):
    if comp_letter == "O":
        player_letter = "X"
    else:
        player_letter = "O"
    #goes through the duplicate board for a winning AI position
    for i in range(1,len(board)):
        copy = clone_board(board)
        if copy[i] == " " :
            copy[i] = comp_letter
            if check_win(copy, comp_letter):
                return i
    #goes through the duplicate board for a winning player position
    for i in range(1,len(board)):
        copy = clone_board(board)
        if copy[i] == " " :
            copy[i] = player_letter
            if check_win(copy, player_letter):
                return i
    #if the center is free, places there. Then checks the corners
    #then the rest.
    if board[5] == " " :
        return 5
    else:    
        move = random_move(board, [1, 3, 7, 9])
        if move != None:
            return move
    return random_move(board, [2, 4, 6, 8])

print_dog()
print_menu()
while True:
    menu_choice = input("Choose from the menu: ")
    if menu_choice == "1":
        first_player = input("Name of the first player: ")
        second_player = input("Name of the second player: ")
        break
    elif menu_choice == "2":
        first_player = input("Name of the player: ")
        second_player = "Computer"
        break
    elif menu_choice == "3":
        print_instruction()
        continue
    elif menu_choice == "4":
        exit()
    else:
        print("Not a valid choice!")
        continue

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    win = False
    count = 0
    board = [" "] * 10
    while not win:
        if count % 2 == 0:
            letter = "X"
        else:
            letter = "O"
        show_board(board)
        #move order needs to be changed depending on which player is the Computer
        if first_player == "Computer":
           if count % 2 == 0:
               make_move = computer_move(board, letter)
               board[make_move] = letter
           else:
               make_move = get_input()
               board[make_move] = letter
        elif second_player == "Computer":
            if count % 2 == 0:
                make_move = get_input()
                board[make_move] = letter
            else:
               make_move = computer_move(board, letter)
               board[make_move] = letter
        #Both players are human       
        else:
            make_move = get_input()
            board[make_move] = letter
       
        os.system('cls' if os.name == 'nt' else 'clear')
        count += 1

        #Congratulate the winner, then switch the players.
        if check_win(board, letter) == True:
            show_board(board)
            if letter == "X":
                print("Hooray!", first_player," won the game!")
            else:    
                print("Hooray!", second_player," won the game!")
            win = True
            c = first_player
            first_player = second_player
            second_player = c

        #if the move counter reaches 9 and there's no winner, it's a draw.
        if count == 9 and win == False:
            show_board(board)
            print("It's a draw!")
            c = first_player
            first_player = second_player
            second_player = c
            break

    if not new_game():
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')





   

