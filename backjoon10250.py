t = int(input())

for i in range(0, t):
  h, w, n = map(int, input().split())

  if n % h == 0:
    l = n // h
  else:
    l = n // h + 1
  f = n - (l - 1) * h
  print(f*100 + l)