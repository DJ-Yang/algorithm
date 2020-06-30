a, b, v = map(int, input().split())

h = v - a

d = h // (a - b)

if h % (a - b) == 0:
  print(d + 1)
else:
  print(d + 2)