

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        counter = 0
        right = 3
        hash_table = {}
        count_num = 0  
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        for i in range(len(grid) - right + 1):
            for j in range(len(grid[0]) - right + 1):
                window = [row[j : j + right] for row in grid[i : i + right]]
                hash_table[counter] = window
                counter += 1

        for values in hash_table.values():
            status = True

            for i in range(len(values)):
                for j in range(len(values[i])):
                    if values[i][j] > 9:
                        status = False
                        break
                if not status:
                    break

            if status:
                for row in values:
                    if sum(row) != 15:
                        status = False
                        break

            if status:
                num_cols = len(values[0])
                for col in range(num_cols):
                    col_sum = 0
                    for row in values:
                        col_sum += row[col]
                    if col_sum != 15:
                        status = False
                        break

            if status:
                main_diag_sum = sum(values[i][i] for i in range(right))
                anti_diag_sum = sum(values[i][right - 1 - i] for i in range(right))

                if main_diag_sum != 15 or anti_diag_sum != 15:
                    status = False

            if status:
                distinct = {num for row in values for num in row}
                if len(distinct) != 9:
                    status = False

            if status:
                count_num += 1  

        return count_num
