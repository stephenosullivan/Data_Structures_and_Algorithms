__author__ = 'stephenosullivan'

import sys


# front-end   back-end
#   0 ----------->     # New Game is initiated by the front-end code
#   <----------- 0     # Back-end code says OK.
#   2 M --------->     # Human Move followed by Move Value M which is 0-6.
#                      # Move Value M will be on separate line.
#   <----------- 0     # Back-end code says OK.
#   1 ----------->     # Computer Move is indicated to back-end code.
#   <--------- 0 M     # Status OK and Move Value M which is 0-6.
#   3 ----------->     # Game Over?
#   <--------- Val     # Val is 0=Not Over, 1=Computer Won, 2=Human Won, 3=Tie.


def minimax(player, board):
    if player == 1:
        #find max
        pass
    else:
        #find min
        pass

if __name__ == '__main__':
    initialsignal = next(sys.stdin).rwrite()