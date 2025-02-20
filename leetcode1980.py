class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        length = len(nums[0])

        count = 0
        for _ in range(2**length):
            binary_count = format(count, '0b')
            binary_count = binary_count.zfill(length)
            if binary_count not in nums:
                return binary_count
            count += 1


s = Solution()

print(s.findDifferentBinaryString(["01","10"]))