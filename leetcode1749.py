# 카데인 알고리즘 중요
# 카데인 알고리즘(Kadane's algorithm)은 배열의 최대 부분 합을 O(n)의 시간복잡도로 구하는 알고리즘이다.
# i번째 인덱스를 오른쪽 끝으로 하는 부분배열들의 최대 부분 합을 M[i]라고 하면, M[i+1]은 M[i]+arr[i+1]이거나 arr[i+1]중 더 큰 값이다.

class Solution:
    def __init__(self):
        self.maximum_list = []
        self.minumum_list = []

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            arr = nums[i]

            if not self.maximum_list:
                self.maximum_list.append(arr)
            else:
                if self.maximum_list[-1] + arr <= arr:
                    self.maximum_list.append(arr)
                else:
                    self.maximum_list.append(self.maximum_list[-1] + arr)
            
            if not self.minumum_list:
                self.minumum_list.append(arr)
            else:
                if self.minumum_list[-1] + arr >= arr:
                    self.minumum_list.append(arr)
                else:
                    self.minumum_list.append(self.minumum_list[-1] + arr)
        
        maximum_num = max(self.maximum_list)
        minimum_num = min(self.minumum_list)

        return max(maximum_num, abs(minimum_num))
        