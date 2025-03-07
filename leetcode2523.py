class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        a = [False,False] + [True]*(right-1)
        primes = []

        for i in range(2,int(right ** 0.5) + 1):
            if a[i]:
                for j in range(2*i, right+1, i):
                    a[j] = False

        primes = [i for i in range(left, right +1) if a[i]]

        if len(primes) < 2:
            return [-1, -1]

        diff = right + 1 - left
        minimum = [-1, right + 1]
        for i in range(1, len(primes)):
                inner_diff = primes[i] - primes[i - 1]
                if inner_diff < diff:
                    diff = inner_diff
                    minimum = [primes[i - 1], primes[i]]
        return minimum

## 에라토스테네스의 체 중요(절반까지만 체크하면 된다..)
            
        
        