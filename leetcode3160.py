# Time Limit
# class Solution:
#     def queryResults(self, limit: int, queries):
#         color_map = dict()
#         result = []
#         for query in queries:
#             color_map[query[0]] = query[1]
#             result.append(len(set(color_map.values())))
#             print(color_map)

#         return result
# set을 사용해서 중복을 제거하니 시간 복잡도가 반복문*set으로 n^2가 나오기 때문에 시간 측정에서 실패했다. Big-O : n^2

# 아래 코드는 dict의 삽입과 삭제를 이용하기 때문에 반복문 * 1 * 1.... 형식으로 시간 복잡도가 나오기 때문에 Big-O : n의 시간복잡도가 나오게 된다.(솔루션 봤음))
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_map = {}
        color_map = {}
        result = []

        for ball, color in queries:
            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1
                if color_map[prev_color] == 0:
                    del color_map[prev_color]
            
            ball_map[ball] = color
            if color in color_map:
                color_map[color] += 1
            else:
                color_map[color] = 1
            result.append(len(color_map))
        
        return result