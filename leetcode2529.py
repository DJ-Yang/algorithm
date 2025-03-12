class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        zero = 0
        for num in nums:
            if num < 0:
                count += 1
                continue
            elif num == 0:
                zero += 1
                continue
            else:
                break

        return max(count, length - count - zero)