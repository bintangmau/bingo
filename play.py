from numpy.matrixlib.defmatrix import matrix
from board import board as generate_board, Board
from shuffle_number import shuffle
import numpy as np

class Play:
    
    def __init__(self) -> None:
        self.board = generate_board
        self.round_now = 0
        self.check_win
        self.check
        self.results = []
        self.win_condition  = np.full(shape=5, fill_value=True, dtype=np.bool)
        self.win_pattern = [
            list(range(1, 6)), 
            list(range(6, 11)),  
            list(range(11, 16)), 
            list(range(16, 21)),
            list(range(21, 26)),
            [1, 7, 13, 19, 25],
            [5, 9, 13, 17, 21]
        ]
        
    def check(self):
        c_idx = 0
        num = shuffle[self.round_now]
        self.check_win()
        print("Check ...", num)
        for x in self.board[0]:
            for y in x:
                c_idx += 1
                if(num == y):
                    print("Matching ...")
                    idx = np.where(x == num)
                    x[idx[0][0]] = 0
                    self.results.append(c_idx)
                    print(matrix(self.board[0]))
                
    def check_win(self):    
        for y in self.win_pattern:
            is_in = np.isin(y, self.results)
            compare = self.win_condition == is_in 
            is_equal = compare.all() 
            if is_equal:
                print("=============================== BINGO !!! =========================")
                self.board = Board.generate_board()
                self.round_now = 0
                self.results = []
                
    def next_match(self):
        self.check()
        if self.round_now == 74:
            self.round_now = 0
        self.round_now += 1
        
play = Play()
next_match = play.next_match