class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern_length = len(pattern)
        pattern_list = list(pattern)

        stack = []
        result = []
        for i in range(pattern_length + 1):
            count = i + 1
            if  not pattern_list or pattern_list.pop(0) == 'D':
                stack.append(count)
                continue

            result.append(count)
            if stack:
                while stack:
                    result.append(stack.pop())
            
        if stack:
            while stack:
                result.append(stack.pop())

        return ''.join(str(s) for s in result)
                                
s = Solution()

print(s.smallestNumber(pattern="IIIDIDDD"))


        