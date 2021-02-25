import random

class Shuffled:
    
    def __init__(self, arr, n) -> None:
        self.arr = arr
        self.n = n

    def randomize (self):
        for i in range(self.n - 1, 0, -1): 
            j = random.randint(0, i) 
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i] 
        return self.arr 


class Number:
    
    def __init__(self) -> None:
        pass
    
    def arr():
        arr = []    
        for i in range(75):
            arr.append(i + 1)
        return arr

arr = Number.arr() 
shuffle = Shuffled(arr, len(arr)).randomize()
