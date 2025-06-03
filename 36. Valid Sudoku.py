class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] #3*3 boxes

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                # check row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                #check column
                if val in columns[c]:
                    return False
                columns[c].add(val)

                #check 3*3 box
                box_index = (r // 3) * 3 + (c // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
        return True
