class Solution:
    def check_square(self, grid, row, column, current_value):
        length = len(grid)
        if row < 0 or row > length - 1 or column < 0 or column > length - 1:
            return -1

        if grid[row][column] != (current_value + 1):
            return -1

        return max(
            current_value + 1,
            self.check_square(grid, row + 2, column + 1, current_value + 1),
            self.check_square(grid, row + 2, column - 1, current_value + 1),
            self.check_square(grid, row + 1, column + 2, current_value + 1),
            self.check_square(grid, row + 1, column - 2, current_value + 1),
            self.check_square(grid, row - 1, column + 2, current_value + 1),
            self.check_square(grid, row - 1, column - 2, current_value + 1),
            self.check_square(grid, row - 2, column + 1, current_value + 1),
            self.check_square(grid, row - 2, column - 1, current_value + 1),
        )

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        return len(grid)*len(grid) - 1 == self.check_square(grid, 0, 0, -1)

s = Solution()
print(s.checkValidGrid(grid=[[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]))