# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 08:13:37 2016

@author: Wickramaranga
"""

#!/usr/bin/python

def nearest_dirty_cell(posr, posc, dimx, dimy, board):
    distances = {}
    for r in range(dimy):
        for c in range(dimx):
            if board[r][c] == "d":
                distance = abs(r-posr) + abs(c-posc)
                if distance not in distances:
                    distances[distance] = [(r, c)]
                else:
                    distances[distance] += [(r, c)]
    
    minimum_distance = min(distances.keys())
    return distances[minimum_distance][0]
                
        
# Head ends here
def next_move(posr, posc, dimx, dimy, board):
    if board[posr][posc] == "d":
        print("CLEAN")
    else:
        r, c = nearest_dirty_cell(posr, posc, dimx, dimy, board)
        
        if r < posr: 
            print("UP")
        elif c < posc:
            print("LEFT")
        elif c > posc:
            print("RIGHT")
        elif r > posr:
            print("DOWN")
        else:
            assert False


# Tail starts here
if __name__ == "__main__":
    x, y = [int(i) for i in input().strip().split()]
    h, w = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(h)]
    next_move(x, y, w, h, board)
