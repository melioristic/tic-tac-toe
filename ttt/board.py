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

class TTTBoard(object):
    def __init__(self, state = None):
        """Main board of Tic Tac Toe

        Args:
            state (Int, optional): 0 or 1 for O and X. Defaults to None.
        """
        if state != None:
            self.state = state
        else:
            self.state = [[] for i in range(9)]

    def show_board(self):
        """
        Basic code for visualisation of the board
        """
        for i in range(3):
            start = 3*i
            # print(f"{self.state[start]} | {self.state[start+1]} | {self.state[start+2]}")
            print(self._convert01OX(self.state[start])) 
            print(self._convert01OX(self.state[start+1])) 
            print(self._convert01OX(self.state[start+2])) 
              
            if i<2:
                print("-------------")

    def _convert01OX(self, element):
        if element==[0]:
            element="[O]"
        elif element==[1]:
            element= "[X]"
        else:
            element = "[ ]"

        return element