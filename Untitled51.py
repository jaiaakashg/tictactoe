#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def print_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0
    max_moves = 9
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while moves < max_moves:
        try:
            row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
            
            if board[row][col] != " ":
                print("Cell already taken, choose another one.")
                continue
            
            board[row][col] = current_player
            moves += 1
            print_board(board)
            
            if check_winner(board, current_player):
                print(f"Congratulations! Player {current_player} wins!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as 0, 1, or 2.")
    
    if moves == max_moves:
        print("It's a tie!")

# Run the game
tic_tac_toe()


# In[ ]:




