import math
import sys

max_int = 7500000
sqrt_int = int(math.sqrt(max_int))
prime_bool = [1] * (max_int)
prime_list = []

# 에라스트체
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

num = int(input(''))

start = 2
while len(prime_list) <= num - 1:
  if (prime_bool[start] == 1):
    prime_list.append(start)
  start = start + 1

print(prime_list[num - 1]) 

  