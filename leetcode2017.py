# import copy

# class Solution:
#     def _get_biggest_sum_path(self, grid, row, column, total_sum, path, m):
#         path = copy.deepcopy(path)
#         total_sum += grid[row][column]
#         path.append((row, column))

#         if row == 1 and column == m - 1:
#             return total_sum, path

#         if row < 1 and column == m - 1:
#             return self._get_biggest_sum_path(grid, row + 1, column, total_sum, path, m)

#         if row == 1 and column < m - 1:
#             return self._get_biggest_sum_path(grid, row, column + 1, total_sum, path, m)


#     def gridGame(self, grid) -> int:
#         m = len(grid[0])
        
#         _, first_path = self._get_biggest_sum_path(grid, 0, 0, 0, [], m)

#         print(first_path)

#         for row, column in first_path:
#             grid[row][column] = 0

#         result, _ = self._get_biggest_sum_path(grid, 0, 0, 0, [], m)

#         return result


class Solution:
    def gridGame(self, grid) -> int:
        result = []
        top_sum = sum(grid[0])
        bottom_sum = 0
        for i in range(len(grid[0])):
            top_sum -= grid[0][i]
            if i > 0:
                bottom_sum += grid[1][i-1]
            result.append(max(top_sum, bottom_sum))
        return min(result)
        

s = Solution()

print(s.gridGame(grid=[[2,5,4],[1,5,1]]))
# print(s.gridGame(grid=[[3,3,1],[8,5,2]]))
# print(s.gridGame(grid=[[1,3,1,15],[1,3,3,1]]))
# print(s.gridGame(grid=[[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]))
