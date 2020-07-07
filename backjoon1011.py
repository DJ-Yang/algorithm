t = int(input())

for c in range(0, t):
  x, y = map(int, input().split())

  n = y - x

  i = 1

  while True:
    if n <= (i * i) + i:
      break
    else:
      i += 1
  if n / i > i:
        print(2*i)
  else:
    print(2*i-1)
    