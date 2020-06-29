k = int(input())

n = k // 3

for i in range(0, n+1):
  if (k - (3 * i)) % 5 == 0:
    s = (k - (3 * i)) // 5
    print(s + i)
    break
  if i == n:
    print(-1)