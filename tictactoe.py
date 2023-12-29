# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:06:42 2022

@author: sid
"""

import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, main):
        pass
    
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, main):
        square = random.choice(main.available_moves())
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, main):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter +'\'s turn. Input moves(0-9)')
            try:
                val = int(square)
                if val not in main.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid input')
            
        return val 