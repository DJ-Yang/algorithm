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



## 다른 사람 정답이라는데 너무 어렵다..

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track last position of a, b, c
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last position of current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Add count of valid substrings ending at current position
            # If any character is missing, min will be -1
            # Else min gives leftmost required character position
            total += 1 + min(last_pos)

        return total

        