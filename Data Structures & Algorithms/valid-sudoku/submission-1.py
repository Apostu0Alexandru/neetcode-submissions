class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set()for _ in range(9)]
        boxes = [set()for _ in range(9)]
        r = 0
        c = 0
        while(r<9):
            while(c<9):
                val = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)
                if val == ".":
                    c+=1
                    continue
                if val in rows[r]:
                    return False
                else:
                    rows[r].add(val)

                if val in cols[c]:
                    return False
                else:
                    cols[c].add(val)
                if val in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].add(val)
                c+=1
            c = 0
            r += 1

        return True