# 해설을 봤지만 왜 수학적인 해석에 대한 이해가 아직 안됐다..
# r - l <= 2*k 일 경우 해당하는 건 알겠는데,
# l이 증가할 때 왜 -1을 해야할까..

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        
        result = 0
        r_index = 0
        l_index = 0
        count = 0

        while r_index < len(sorted_nums):
            if sorted_nums[r_index] - sorted_nums[l_index] <= 2*k:
                r_index += 1
                count += 1
                continue
            
            l_index += 1
            result = max(result, count)
            count -= 1
        
        return max(result, count)
