import math
import sys

max_int = 246913
sqrt_int = int(math.sqrt(max_int))
prime_bool = [1] * (max_int)
prime_list = []

# 에라토스테네스의 체
def check_prime():
  prime_bool[0] = 0
  prime_bool[1] = 0
  a = 2
  while a <= sqrt_int:
    if prime_bool[a] == 1:
      b = a*a
      while b <= max_int:
        try:
          prime_bool[b] = 0
          b = b + a
        except:
          b = b + a
        
    a = a + 1
check_prime()

while True:
  n = int(input())

  if n == 0:
    break
  prime_list = []
  f = 2 * n

  for i in range(n+1, f + 1):
    if (prime_bool[i] == 1):
      prime_list.append(i)

  print(len(prime_list))