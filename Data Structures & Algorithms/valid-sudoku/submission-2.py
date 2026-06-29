class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            x = set(i)
            if len(x) - 1 != len([y for y in i if y != '.']):
                return False

        for y in range(len(board)):
            s = set()
            arr = []
            for x in range(len(board)):
                s.add(board[x][y])
                if board[x][y] != '.':
                    arr.append(board[x][y])
            if len(s) -1 != len(arr):
                return False

        for y in range(0, len(board), 3):
            for x in range(0, len(board), 3):
                s = set()
                arr = []
                for i in range(3):
                    for j in range(3):
                        s.add(board[x+j][y+i])
                        if board[x+j][y+i] != '.':
                            arr.append(board[x+j][y+i])
                if len(s) -1 != len(arr):
                    return False
        
        return True
