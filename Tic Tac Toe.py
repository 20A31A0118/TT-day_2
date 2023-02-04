#TIC TAC TOE
board = [['','',''],['','',''],['','','',]]

def print_board(board):
    print(*board[0], sep=" | ")
    print("__________")
    print(*board[1], sep=" | ")
    print("__________")
    print(*board[2], sep=" | ")
def get_marker():
    marker1 = input("Player 1 choice(x or o): ").upper()
    marker2 = ""
    if marker1 == "X":
        marker2 = 'o'
        return ['X', 'O']
    elif marker1 == 'O':
        marker2 = 'x'
        return ['O', 'X']
    else:
        print("Invalid Input")
        return get_marker()
def get_coordinate():
    x,y = list(map(int, input("Enter the coordinates:").split()))
    if x in [0,1,2] and y in [0,1,2]:
        return [x,y]
    else:
        print("Invalid Input")
        return get_coordinate()
def check_for_win(board):
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[1] != "":
            return True
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] != "":
            return True
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != "":
            return True
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != "":
            return True
        return False
def update_board(board, chance, marker, x,y):
    if chance == True:
        board[x][y] = marker
        if check_for_win(board):
            print("Player 1 wins")
            return "game over"
        return False
    else:
        board[x][y] = marker
        if check_for_win(board):
            print("Player 2 wins")
            return "game over"
        return True
def play_game():
    player1 = 0
    player2 = 0
    m1, m2 = get_marker()
    print(f"player 1: {m1}, player 2: {m2}")
    chance = True
    while True:
        print_board(board)
        x, y = get_coordinate()
        if chance:
            chance = update_board(board, chance, m1, x,y)
            if chance == "game over":
                break
        else:
            chance = update_board(board, chance, m2, x,y)
            if chance == "game over":
                break
play_game()


'''output:
    Player 1 choice(x or o): x
player 1: X, player 2: O
 |  | 
__________
 |  | 
__________
 |  | 
Enter the coordinates: 1 1
 |  | 
__________
 | X | 
__________
 |  | 
Enter the coordinates: 2 2
 |  | 
__________
 | X | 
__________
 |  | O
Enter the coordinates: 0 1
 | X | 
__________
 | X | 
__________
 |  | O
Enter the coordinates:1 2
 | X | 
__________
 | X | O
__________
 |  | O
Enter the coordinates: 0 1
 | X | 
__________
 | X | O
__________
 |  | O
Enter the coordinates: 0 0
O | X | 
__________
 | X | O
__________
 |  | O
Enter the coordinates: 0 2
O | X | X
__________
 | X | O
__________
 |  | O
Enter the coordinates: 2 1
O | X | X
__________
 | X | O
__________
 | O | O
Enter the coordinates: 2 0
Player 1 wins'''

