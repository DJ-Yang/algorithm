
# Time Lmit Exceeded
# class Solution:
#     def numOfSubarrays(self, arr: List[int]) -> int:
#         count = 0
#         for i in range(len(arr)):
#             num = arr[i]
#             if num % 2 == 1:
#                 count += 1
#             for j in range(i + 1, len(arr)):
#                 num += arr[j]
#                 if num % 2 == 1:
#                     count += 1
#         return count

# 하위 배열에서의 개수를 계속 기억해두고 그 다음값에 이용한다. 예를 들어 하위에서 홀수 개수가 3이고 이번 숫자와 더해서 나온 것이 짝수라면
# 홀수가 3개가 추가된다고 생각하면 된다. 대신 이번엔 짝수기 때문에 짝수 하위 배열이 하나 추가됐다고 생각해야한다.. 대단하다.
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        num_sum = 0
        result = 0
        odd = 0
        even = 1

        for i in range(len(arr)):
            num_sum += arr[i]

            if num_sum % 2 == 1:
                result += even
                odd += 1
            else:
                result += odd
                even += 1

        return result % (10**9 + 7)

s = Solution()

print(s.numOfSubarrays(arr=[2,4,6]))