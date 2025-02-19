class Solution:
    def create_str(self, n: int, result: list, before_word: str ='', word: str = ''):
        letters = ['a', 'b', 'c']

        for i in range(len(letters)):
            if before_word == letters[i]:
                continue
            current_word = word
            current_word += letters[i]
            if len(current_word) == n:
                result.append(current_word)
                continue
            self.create_str(n, result, letters[i], current_word)
        
    def getHappyString(self, n: int, k: int) -> str:
        result = []

        self.create_str(n, result)

        if len(result) < k:
            return ""
        return result[k - 1]


s = Solution()

# print(s.getHappyString(n=1, k=3))
# print(s.getHappyString(n=1, k=4))
print(s.getHappyString(n = 3, k = 9))
