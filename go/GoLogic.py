class Board():
    # list of all 8 directions on the board, as (x,y) offsets
    __directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

    def __init__(self, n):
        self.n = n

        # Create empty board 2-d array
        self.pieces = [None]*self.n
        for i in range(self.n):
            self.pieces[i] = [0]*self.n

    def get_legal_moves(self, color):
        return list()

    def has_legal_moves(self, color):
        return False