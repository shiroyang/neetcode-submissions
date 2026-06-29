class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(l):
            c = Counter(l)
            for key, val in c.items():
                if val > 1 and key != '.':
                    return False
            return True

        for i in range(9):
            row = board[i][:]
            if not is_valid(row): 
                return False
        
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not is_valid(col):
                return False

        for i in range(3):
            for j in range(3):
                tmp = []
                for di in range(3):
                    for dj in range(3):
                        tmp.append(board[3*i+di][3*j+dj])
                if not is_valid(tmp):
                    return False

        return True