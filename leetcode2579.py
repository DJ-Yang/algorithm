class Solution:
    def coloredCells(self, n: int) -> int:
        result = 1
        num = 1
        while num <= n:
            result += 4 * (num - 1)
            num += 1

        return result
        
# 간단한 수학 문제였는데, 조금 더 수학 공부를 할 필요성이 느껴진다.
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2
        