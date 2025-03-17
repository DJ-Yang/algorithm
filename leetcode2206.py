class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        length = len(nums)
        n = length // 2

        data = dict()
        for i in range(length):
            if nums[i] in data:
                data[nums[i]] += 1
            else:
                data[nums[i]] = 1

        num = [value // 2 for value in data.values()]
        if sum(num) >= n:
            return True
        return False
        