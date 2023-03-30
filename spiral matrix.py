class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        start_row = 0
        start_col = 0

        end_row = row
        end_col = col

        curr_row = 0
        curr_col = col - 1

        spiral = []

        while(len(spiral) < row*col):
            
            #Left -> Right
            for i in range(curr_row, end_col):
                spiral.append(matrix[curr_row][i])
            curr_row += 1
            end_col -= 1

            if len(spiral) == row*col:
                break
            
            # Top right -> Top down
            for i in range(curr_row, end_row):
                spiral.append(matrix[i][curr_col])
            curr_col -= 1
            end_row -= 1

            if len(spiral) == row*col:
                break
            
            #Bottom Right -> Bottom Left
            for i in range(curr_col, start_col-1, -1):
                spiral.append(matrix[end_row][i])
            start_col += 1

            if len(spiral) == row*col:
                break
            
            #Bottom left -> Top Left
            for i in range(end_row-1, start_row, -1):
                spiral.append(matrix[i][start_col-1])
            start_row += 1
        return spiral
