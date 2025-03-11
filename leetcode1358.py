class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length = len(s)
        alphabet_dict = {'a': 0, 'b': 0, 'c': 0}

        start = 0
        end = 0
        result = 0

        while end < length:
            alphabet_dict[s[end]] += 1

            while min(alphabet_dict.values()) != 0:
                if start == end:
                    break
                result += length - end
                alphabet_dict[s[start]] -= 1
                start += 1
            end += 1
        
        result += length - end

        return result

s = Solution()

print(s.numberOfSubstrings(s = "abcabc"))


        