n = int(input())

for i in range(1, 2*n):
  if i <= n:
    for a in range(1, i):
      print(' ', end='')
    for a in range(i, 2 * n - i + 1):
      print('*', end='')
  else:
    for a in range(1, 2 * n - i):
      print(' ', end='')
    for a in range(2 * n - i, i + 1):
      print('*', end='')
  print('')