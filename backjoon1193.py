k = int(input())

n = 1

while True:
  if k <= n * (n + 1) / 2:
    r = int(k - (n * (n - 1) / 2))
    if n % 2 == 0:
      print("{0}/{1}".format(r, n - r + 1))
    else:
      print("{0}/{1}".format(n - r + 1, r))
    break
  n += 1