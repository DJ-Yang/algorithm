k = int(input())

n = 0

while True:
  if k <= (3 * n * n) + (3 * n) + 1:
    print(n+1)
    break
  n += 1