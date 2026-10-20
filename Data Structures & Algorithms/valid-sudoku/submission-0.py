class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                seen.add(board[i][j])

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen and board[j][i] != '.':
                    return False
                seen.add(board[j][i])
        

        for box_r in range(3):
            for box_c in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[box_r * 3 + i][box_c * 3 + j] in seen and board[box_r * 3 + i][box_c * 3 + j] != '.':
                            return False
                        seen.add(board[box_r * 3 + i][box_c * 3 + j])

        return True