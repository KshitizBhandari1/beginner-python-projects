#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:38:56 2020

@author: kshitizbhandari

Tic-Tac-Toe

A game of tic-tac-toe, where the board is visualized as:
    1   2   3
    4   5   6
    7   8   9
    (numbers mark the position)
"""

import random

game_board = [position for position in range(0, 9)]

# initialize player and computer
player, computer = '', ''

## Define the moevs
# the board is visualized as follows
# 1 # 2 # 4
# 4 # 5 # 6
# 7 # 8 # 9

# positions for corners, center, and remaining locations
# 4 corners, 1 center, and 4 remaining
moves = ( (1, 3, 7, 9), (5,), (2, 4, 6, 9))

## Winning combinations
# indices of the board positions that guarantee a win

winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), # three horizontal rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), # three vertical rows
                        (0, 4, 8), (2, 4, 6)) # two diagonals

# Table
tab = range(1, 10)

## Display board in CUI
def display_board():
    '''
    prints the tic-tac-toe board in CUI
    Returns
    -------
    None
    '''
    # note position is 1 greater than the game_board index
    position = 1
    
    for i in game_board:
        end = ' | '     # vertical bar after each space
        if position % 3 == 0: # end of each row (three spaces)
            end = '\n'  # change row after three spaces
            if i not in [0, 8]:
                end += '---------\n' # add horizontal bar between rows
            
            if i == 8:
                end += '=================\n'
                
        char = ' '      # empty if the space isn't used yet
        
        if i in ('X', 'O'):
            char = i    # if space is filled, use respective character
        
        print(char, end = end)
        position += 1    # move on to the next position


def select_character():
    '''
    Returns
    -------
    Either ('X', 'O') or ('O', 'X') at random.

    '''
    chars = ('X', 'O')
    
    # generate character sequence at random
    if random.randint(0, 1) == 0:
        return chars[::-1]

    # returns either ('X', 'O') or ('O', 'X')    
    return chars


def can_move(board, player, move):
    if move in tab and board[move - 1] == move - 1:
        return True
    return False


def can_win(board, player, move):
    '''
    Tests if the player can win

    Parameters
    ----------
    board : List
        Symbolizing tic-tac-toe board
    player : string
        Either 'X' or 'O'
    move : int
        move for a player

    Returns
    -------
    win : bool
        Whether the player can win or not

    '''
    places = []
    x = 0
    
    for i in board:
        if i == player:
            places.append(x)
        x += 1
    win = True
    
    for tup in winning_combinations:
        win = True
        for ix in tup:
            if board[ix] != player:
                win = False
                break
        if win == True:
            break
    return win


# make move for the current board situation and given player
def make_move(board, player, move, undo = False):
    '''
    Make move for the current board situation and given player

    '''          
    if can_move(board, player, move):
        board[move-1] = player
        win = can_win(board, player, move)
    
                  
        if undo:
            board[move - 1] = move - 1
        return(True, win)
    
    return (False, False)


def computer_move():
    '''
    Select computer's move

    '''
    move = -1
    # If computer can win, player does not matter.
    # Brute force
    for i in range(1, 10):
        if make_move(game_board, computer, i, True)[1]:
            move = i
            break
        
    if move == -1:
        # If player can win, block the player's winning place.
        for i in range(1, 10):
            if make_move(game_board, player, i, True)[1]:
                move = i
    
    if move == -1:
        #Otherwise, try to take a favorable place.
        for j in moves:
            for mv in j:
                if move == -1 and can_move(game_board, computer, mv):
                    move = mv
                    break
    return make_move(game_board, computer, move)



def space_exist():
    '''
    Test if the board is full or not
    Returns: True or False
    '''
    return game_board.count('X') + game_board.count('O') != 9


# select and display character for user and computer
player, computer = select_character()
print("Player is '%s' and computer is '%s'" % (player, computer))

# initialize result
result = '%%% It is a tie! %%%'


# until the board is full
while space_exist():
    display_board()
    print('# Make your move! Select position [1-9] : ', end = '')
    
    move = int(input())
    moved, won = make_move(game_board, player, move)
    
    # check if the move is valid
    if not moved:
        print('>>> This choice is invalid! Please, try again.')
        continue
    
    if won:
        result = '*** CONGRATULATIONS! You are the winner! ***'
        break
    
    # if computer's move results in the computer winning
    elif computer_move()[1]:
        result = "=== Unfortunately, the computer wins! ==="
        break


display_board()
print(result)


    
    
    
    
    
    