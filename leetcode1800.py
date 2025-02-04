class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum = 0
        sum_list = []
        num_len = len(nums)
        
        for i in range(num_len):
            n = i + 1
            if n == num_len:
                current_sum += nums[i]
                sum_list.append(current_sum)
                break
            
            if nums[i] >= nums[n]:
                current_sum += nums[i]
                sum_list.append(current_sum)
                current_sum = 0
                continue

            current_sum += nums[i]

        return max(sum_list)
