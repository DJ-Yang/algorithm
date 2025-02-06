# 메모리 부족으로 실패
# from itertools import permutations

# class Solution:
#     def tupleSameProduct(self, nums: List[int]) -> int:
#         count = 0
#         uniqued_nums = tuple(nums)
#         if len(uniqued_nums) < 4:
#             return count
#         per_uniqued_nums = list(permutations(uniqued_nums, 4))

#         for nums in per_uniqued_nums:
#             if nums[0] * nums[1] == nums[2] * nums[3]:
#                 count += 1

#         return count

# 곱한 숫자를 가져와서 (a,b,c,d)를 구한 후 하나당 *8을 진행하는 방식
# 곱한 숫자를 키로 갖는 값이 총 2개 일경우 -> 경우의 수 1
# 곱한 숫자를 키로 갖는 값이 총 3개일 경우 -> 경우의 수 3, (x, y, z) -> (x, y), (x, z), (y, z)
# 즉, n * (n - 1) / 2
class Solution:
    def tupleSameProduct(self, nums):
        count = 0

        if len(nums) < 4:
            return count
        num_dict = dict()

        for i in range(len(nums)):
            for num in nums[i + 1:]:
                if nums[i]*num in num_dict:
                    num_dict[nums[i]*num] += 1
                else:
                    num_dict[nums[i]*num] = 1

        for _, value in num_dict.items():
            if value < 2:
                continue
        
            count += value*(value-1)/2
        return int(count * 8)


s = Solution()

print(s.tupleSameProduct([2,3,4,6]))
print(s.tupleSameProduct([1,2,4,5,10]))
print(s.tupleSameProduct([2,3,4,6,8,12]))
