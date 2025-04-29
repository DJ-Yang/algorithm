class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        global_max = max(nums)
        count = 0
        result = 0
        left = 0

        for right, val in enumerate(nums):
            if val == global_max:
                count += 1
            
            while count >= k:
                result += len(nums) - right
                if nums[left] == global_max:
                    count -= 1
                left += 1

        return result