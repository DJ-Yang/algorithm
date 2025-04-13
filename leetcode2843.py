class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        for i in range(low, high + 1):
            length = len(str(i))

            if not length % 2 == 0:
                continue

            left = sum(int(n) for n in str(i)[:length // 2])
            right = sum(int(n) for n in str(i)[length // 2:])

            if left == right:
                result += 1

        return result
        