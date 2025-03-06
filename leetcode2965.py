class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        length = len(grid)
        number_map = {i+1: 0 for i in range(length ** 2)}
        for row in grid:
            for column in row:
                number_map[column] += 1

        a = None
        b = None
        for number, value in number_map.items():
            if value == 2:
                a = number
            
            if value == 0:
                b = number
            
            if a and b:
                return [a,b]
