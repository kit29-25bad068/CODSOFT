import math

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("───┼───┼───")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("───┼───┼───")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def print_positions():
    print("\n Position guide:")
    print(" 1 | 2 | 3 ")
    print("───┼───┼───")
    print(" 4 | 5 | 6 ")
    print("───┼───┼───")
    print(" 7 | 8 | 9 ")
    print("\n")

def check_winner(b, player):
    combos = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]      
    ]
    for combo in combos:
        if all(b[i] == player for i in combo):
            return True
    return False

def is_draw(b):
    return " " not in b

def minimax(b, is_maximizing):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"
    print("AI played!")

def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Enter a number between 1 and 9!")
            elif board[move] != " ":
                print("That cell is already taken!")
            else:
                board[move] = "X"
                break
        except ValueError:
            print("Invalid input! Enter a number.")

def play_game():
    global board
    board = [" " for _ in range(9)]
    print("=" * 35)
    print("      Welcome to Tic-Tac-Toe!")
    print("      You are X  |  AI is O")
    print("=" * 35)
    print_positions()

    current = "human"

    while True:
        print_board()

        if current == "human":
            print("Your turn (X):")
            human_move()
            if check_winner(board, "X"):
                print_board()
                print("🎉 Congratulations! You won!")
                break
        else:
            print("AI is thinking...")
            ai_move()
            if check_winner(board, "O"):
                print_board()
                print("🤖 AI wins! Better luck next time!")
                break

        if is_draw(board):
            print_board()
            print("🤝 It's a draw!")
            break

        current = "ai" if current == "human" else "human"

while True:
    play_game()
    again = input("Play again? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("Thanks for playing! Goodbye! 👋")
        break
