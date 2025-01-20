# First Soluntion

# class Solution:
#     def _check_plus_row_zero(self, mat, row, column):
#         if len(mat) <= row:
#             return True
        
#         if mat[row][column] == 0:
#             return self._check_plus_row_zero(mat, row + 1, column)
#         return False

#     def _check_minus_row_zero(self, mat, row, column):
#         if row < 0:
#             return True
        
#         if mat[row][column] == 0:
#             return self._check_minus_row_zero(mat, row - 1, column)
#         return False

#     def _check_plus_column_zero(self, mat, row, column):
#         if len(mat[row]) <= column:
#             return True

#         if mat[row][column] == 0:
#             return self._check_plus_column_zero(mat, row, column + 1)
#         return False

#     def _check_minus_column_zero(self, mat, row, column):
#         if column < 0:
#             return True

#         if mat[row][column] == 0:
#             return self._check_minus_column_zero(mat, row, column - 1)
#         return False

#     def check_row_column_from_value(self, mat, value):
#         for r in range(len(mat)):
#             for c in range(len(mat[r])):
#                 if mat[r][c] == value:
#                     return r, c
                
#     def firstCompleteIndex(self, arr, mat) -> int:
#         for i in range(len(arr)):
#             row, column = self.check_row_column_from_value(mat, arr[i])

#             print(i, row, column)

#             mat[row][column] = 0

#             row_plus_result = self._check_plus_row_zero(mat, row, column)
#             row_minus_result = self._check_minus_row_zero(mat, row, column)
#             column_plus_result = self._check_plus_column_zero(mat, row, column)
#             column_minus_result = self._check_minus_column_zero(mat, row, column)
            

#             if (row_plus_result and row_minus_result) or (column_plus_result and column_minus_result):
#                 return i


# Second Solution (아직도 마지막에 row랑 column 위치 헷갈리긴한다..)
class Solution: 
    def firstCompleteIndex(self, arr, mat) -> int:
        row_len = len(mat)
        column_len = len(mat[0])

        check_row = [0 for _ in range(row_len)]
        check_column = [0 for _ in range(column_len)]

        data_map = dict()
        for row in range(len(mat)):
            for column in range(len(mat[row])):
                data_map[mat[row][column]] = (row, column)

        for i in range(len(arr)):
            row, column = data_map[arr[i]]

            check_row[row] += 1
            check_column[column] += 1

            if column_len == check_row[row] or check_column[column] == row_len:
                return i


s = Solution()

print(s.firstCompleteIndex([1,3,4,2], [[1,4],[2,3]]))
print(s.firstCompleteIndex([2,8,7,4,1,3,5,6,9], [[3,2,5],[1,4,6],[8,7,9]]))
# print(s.firstCompleteIndex([1,4,5,2,6,3], [[4,3,5],[1,2,6]]))

# arr =
# [1,4,5,2,6,3]
# mat =
# [[4,3,5],[1,2,6]]