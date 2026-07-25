class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_size = len(board)
        box_sets = {
            (0,0) : set(),
            (0,1): set(),
            (0,2): set(),
            (1,0) : set(),
            (1,1): set(),
            (1,2): set(),
            (2,0) : set(),
            (2,1): set(),
            (2,2): set()
        }
        #check valid rows
        for i in range(board_size):
            row_set = set()
            for j in range(board_size):
                current_box = (i // 3, j // 3)
                if board[i][j] == ".":
                    pass
                elif board[i][j] in row_set or board[i][j] in box_sets[current_box]:
                    return False
                else:
                    row_set.add(board[i][j])
                    box_sets[current_box].add(board[i][j])

        #check valid columns
        for j in range(board_size):
            column_set = set()
            for i in range(board_size):
                if board[i][j] == ".":
                    pass
                elif board[i][j] in column_set:
                    return False
                else:
                    column_set.add(board[i][j])

        return True