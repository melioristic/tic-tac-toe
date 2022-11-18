#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==========================================================
# Created by : Mohit Anand
# Created on : Sun Nov 13 2022 at 9:47:35 PM
# ==========================================================
# Created on Sun Nov 13 2022
# __copyright__ = Copyright (c) 2022, Mohit Anand's Project
# __credits__ = [Mohit Anand,]
# __license__ = Private
# __version__ = 0.0.0
# __maintainer__ = Mohit Anand
# __email__ = itsmohitanand@gmail.com
# __status__ = Development
# ==========================================================

from colorama import Fore, Back, Style


class TTTBoard(object):
    def __init__(self, state = None):
        """Main board of Tic Tac Toe

        Args:
            state (Int, optional): 0 or 1 for O and X. Defaults to None.
        """
        print(Style.BRIGHT, Fore.GREEN, "=======================", Style.RESET_ALL)
        print(Style.BRIGHT, Fore.GREEN, "Welcome to Tic Tac Toe!", Style.RESET_ALL)
        print(Style.BRIGHT, Fore.GREEN, "=======================", Style.RESET_ALL)

        if state != None:
            self.state = state
        else:
            self.state = [[] for i in range(9)]

        self.player = 0
        self.n_moves = 0

        while self.n_moves<9:
            self.move(self.get_move())
            self.show_board()
            if self.check_win():
                if self.player == 0:
                    col = Fore.YELLOW
                else:
                    col = Fore.CYAN
                print(col, f"Player {self.player} has won!", Style.RESET_ALL)
                break
            self.change_player()

    def show_board(self):
        """
        Basic code for visualisation of the board
        """
        for i in range(3):
            start = 3*i
            print(f"{self._convert01OX(self.state[start])} | {self._convert01OX(self.state[start+1])} | {self._convert01OX(self.state[start+2])}")              
            if i<2:
                print("---------------")

    def _convert01OX(self, element):
        if element==[0]:
            element="[O]"
        elif element==[1]:
            element= "[X]"
        else:
            element = "[ ]"

        return element

    def move(self, position):
        """
        Move of the player

        Args:
            player (Int): 0 or 1 for O and X
            position (Int): Position of the move
        """
        position = (position[0]-1)*3 + position[1]-1
        if self.state[position] != []:
            print(Fore.RED, "Invalid move!")
            print(Style.RESET_ALL)
            return self.move(self.get_move())
        self.state[position] = [self.player]
        self.n_moves += 1
        

    def change_player(self):
        """
        Change the player
        """
        if self.player == 0:
            self.player = 1
        else:
            self.player = 0

    def get_move(self):
        """
        Get the move from the player

        Returns:
            Int: Position of the move
        """
        if self.player == 0:
            col = Fore.YELLOW
        else:
            col = Fore.CYAN
        print(col, f"Player {self.player} move: ", Style.RESET_ALL)
        position = input().split(",")
        position = (int(position[0]), int(position[1]))
        return position

    def check_win(self):
        """
        Check if the player has won

        Returns:
            Bool: True if the player has won
        """
        for i in range(3):
            if self.state[3*i] != [] and self.state[3*i] == self.state[3*i+1] and self.state[3*i] == self.state[3*i+2]:
                return True
            if self.state[i]!= [] and self.state[i] == self.state[i+3] and self.state[i] == self.state[i+6]:
                return True
        if self.state[0] != [] and self.state[0]==self.state[4]==self.state[8]:
            return True
        if self.state[2] != [] and self.state[2]==self.state[4]==self.state[6]:
            return True

        return False


# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)