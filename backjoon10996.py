n = int(input())
  
for i in range(1, n + 1):
  print('*', end='')
  for j in range(1, (n-1)//2 + 1):
    print(' *', end='')
  print('')
  for k in range(1, n//2 + 1):
    print(' *', end='')
  if not n == 1:
    print('')