# 첫 번째 풀이 -> Time Limit Exceeded

# class Solution:
#     def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
#         result = 0
#         length = len(nums)
#         start = 0
#         count = 0
#         while start < length:
#             num = nums[start]
#             end = start

#             if num % modulo == k:
#                 count += 1

#             if count % modulo == k:
#                 result += 1

#             while end < length:
#                 if end == start:
#                     end += 1
#                     continue
                
#                 if nums[end] % modulo == k:
#                     count += 1
                
#                 if count % modulo == k:
#                     result += 1
#                 end += 1
#             count = 0
#             start += 1

#         return result


            
# 으 요즘 진짜 집중 안된다.

class Solution:
    def countInterestingSubarrays(
        self, nums: List[int], modulo: int, k: int
    ) -> int:
        n = len(nums)
        cnt = Counter([0])
        res = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return res
