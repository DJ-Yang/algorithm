# class Solution:
#     def checkPossibleWord(self, count: int, data: dict):
#         count += 1

#         print(count, data)
#         for i in range(len(data)):
#             if data[i] == 0:
#                 continue
                
#             data[i] -= 1
#             count = self.checkPossibleWord(count, data)

#         return count

#     def numTilePossibilities(self, tiles: str) -> int:
#         alphabet_dict = dict()
#         result = 0

#         for tile in tiles:
#             if tile in alphabet_dict:
#                 alphabet_dict[tile] += 1
#             else:
#                 alphabet_dict[tile] = 1

#         for alphabet in alphabet_dict:
#             alphabet_dict[alphabet] -= 1
#             result += self.checkPossibleWord(result, list(alphabet_dict.values()))
#             print("result", result)
#             alphabet_dict[alphabet] += 1

#         return result


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        used = [False] * len(tiles)

        # Generate all possible sequences including empty string
        self._generate_sequences(tiles, "", used, sequences)

        # Subtract 1 to exclude empty string from count
        return len(sequences) - 1

    def _generate_sequences(
        self, tiles: str, current: str, used: list, sequences: set
    ) -> None:
        sequences.add(current)

        # Try adding each unused character to current sequence
        for pos, char in enumerate(tiles):
            if not used[pos]:
                used[pos] = True
                self._generate_sequences(tiles, current + char, used, sequences)
                used[pos] = False


s = Solution()

print(s.numTilePossibilities(tiles="AAB"))
# print(s.numTilePossibilities(tiles="AAABBC"))