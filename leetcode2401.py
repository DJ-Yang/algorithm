# xor을 사용하는 방법 정말 대단하다..

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        maximun_length = 0

        total_sum = 0
        xor_sum = 0

        left = right = 0

        while right < length:
            total_sum += nums[right]
            xor_sum ^= nums[right]

            while total_sum != xor_sum:
                total_sum -= nums[left]
                xor_sum ^= nums[left]
                left += 1

            current = right - left + 1

            if maximun_length < current:
                maximun_length = current
            right += 1

        return maximun_length
