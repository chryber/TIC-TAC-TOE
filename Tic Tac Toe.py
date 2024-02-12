#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Design Board

def board_layout(board):

    
    #Board design to print the values at indexes within the board and space after
    board = [[board[7]  + ' _|_',board[8] + ' _|_',board[9] +  ' _|'],
       
            [  board[4] + ' _|_',board[5] + ' _|_',board[6] + ' _|'],
             
            [  board[1] + ' _|_',board[2] + ' _|_',board[3] +  ' _|']]

    for i in board:
        for j in i:
            print(j, end = "  ")
        print()
    


# In[2]:


## Get user input

def user_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 - Please pick a marker X or O: ').upper()
    
    player1 = marker
    
    player2 = 'O' if player1 == 'X' else 'X'
            
    return (player1, player2)
   


# In[3]:


def put_marker(board, marker, position):
    
    ## Place marker at designated position on the board
    board[position] = marker


# In[4]:


def win_check(board, mark):
    
    ## check if rows have same mark
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))
    
    


# In[5]:


import random

def choose_first():
    
    ## passing the randint function to variable to be referenced within print statement below.
    return random.choice(["Player 1", "Player 2"])


# In[6]:


def blank_space_check(board, position):
    
    ##return true if board position is empty
    
    if board[position] == ' ':
        return True


# In[7]:


def full_board_check(board):
    
    ##checks if board is full
    
    return ' ' not in board[1:]


# In[8]:


def player_choice(board):
    
    position = 0
    
    while position not in range(1,10) or not blank_space_check(board,position):
        position = int(input('Please enter a number (1-9): '))
    return position


# In[9]:


def replay():
    
    return input('Do you want to play again? Y or N: ').upper() == 'Y'


# In[ ]:


print('Welcome to Tic Tac Toe!')
print('Player marker will be placed at the designated value on the board.')
print('Note: Position 1 is at the bottom left and position 9 being at the upper right.')

while True:
    
    ##Sets up board with blank spaces
    board = [' ']*10
    
    #Player marker selection and confirmation of selection
    player1_marker, player2_marker = user_input()
    print('Player 1 is ' +player1_marker)
    print('Player 2 is ' +player2_marker)
    
    ##Assign choose first to turn variable for easier calls
    turn = choose_first()
    print(f'{turn} will be the first to go.')
    ##game in session
          
    while True:
        ##display game board
        board_layout(board)
        
        print(f'Player {turn} your move.')
        position = player_choice(board)
        
        ##place player 1's marker at the designated position on the board
        if turn == 'Player 1':
            put_marker(board, player1_marker, position)
            ##win check
            if win_check(board, player1_marker):
                board_layout(board)
                print('Player 1 is the WINNER!')
                break
            elif full_board_check(board):
                board_layout(board)
                print('The game is a TIE!')
                break
            else:
                turn = 'Player 2'
        
        else:
            #Player 2's turn
            put_marker(board, player2_marker, position)
                ##win check
            if win_check(board, player2_marker):
                board_layout(board)
                print('Player 2 is the WINNER!')
                break
            elif full_board_check(board):
                board_layout(board)
                print('The game is a TIE!')
                break
            else:
                turn = 'Player 1'

    #If players do not want to play, end game
    if not replay():
        print('Thanks for playing, see you again')
        break
    print("\n"*100)    


# In[ ]:




