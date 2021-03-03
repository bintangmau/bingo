from numpy.matrixlib.defmatrix import matrix
from shuffle_number import Shuffled
import numpy as np

class Board:
    
    def __init__(self) -> None:
        pass
        
    def generate_board():
        arr = []
        shuffle_nums = []

        for i in range(75):
            arr.append(i + 1)
        nums = np.array(arr)
        arr = np.split(nums, 5)

        for x in arr:
            selected = []
            shuffled = Shuffled(x).randomize()
            for i in range(len(shuffled)):
                if(i < 5):
                    selected.append(shuffled[i])
            shuffle_nums.append(selected)


        board = np.array([np.hsplit(np.array(shuffle_nums).reshape(5, 5), 5)])
        board[0][2][2][0] = 0
        print("Board is ready ...")
        print(matrix(board[0]))
        return board
    
    
board = Board.generate_board()