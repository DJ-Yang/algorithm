class Solution:

    def countOfSubstrings(self, word: str, k: int) -> int:
        length = len(word)

        vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        start_index = 0
        index = 0
        consonants = 0
        result = 0

        while index < length:
            if word[index] in vowel:
                vowel[word[index]] += 1
            else:
                consonants += 1
            
            if consonants > k:
                while consonants > k:
                    print(start_index, word[start_index])
                    if word[start_index] in vowel:
                        print("in", start_index)
                        vowel[word[start_index]] -= 1
                        if min(vowel.values()) > 0:
                            result += 1
                        start_index += 1
                        continue

                    consonants -= 1
                    print(consonants, k)
                continue
            
            if min(vowel.values()) > 0 and k == consonants:
                result += 1

            index += 1

        return result

s = Solution()
print(s.countOfSubstrings("aeioqq", 1))
# "aeioqq", k = 1

# {'a': 1, 'e': 1, 'i':1, 'o': 1, 'u': 0}