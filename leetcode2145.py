class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        num = lower
        result = 0
        
        while num <= upper:
            value = num
            fail_flag = False
            l = [value]
            for difference in differences:
                value = value + difference

                if value < lower or value > upper:
                    fail_flag = True
                    break
                l.append(value)

            if not fail_flag:
                result += 1
                max_num = max(l)
                result += upper - max_num
                break
            num += 1

        return result


# 정답지
# class Solution:
#     def numberOfArrays(
#         self, differences: List[int], lower: int, upper: int
#     ) -> int:
#         x = y = cur = 0
#         for d in differences:
#             cur += d
#             x = min(x, cur)
#             y = max(y, cur)
#             if y - x > upper - lower:
#                 return 0
#         return (upper - lower) - (y - x) + 1
                