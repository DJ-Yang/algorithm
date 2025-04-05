class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
                continue
            for data in stack[:]:
                stack.append(data^num)
            stack.append(num)

        return sum(stack) if stack else 0