class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)

        count = 0
        for i in range(2, length):
            if nums[i - 2] == 0:
                nums[i - 2] ^= 1
                nums[i - 1] ^= 1
                nums[i] ^= 1
                count += 1

        return -1 if min(nums) == 0 else count