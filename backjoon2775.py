a = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]

def apart():
  for i in range(1, 15):
    b = [1]
    for n in range(1, 14):
      b.append(b[n - 1] + a[i - 1][n])
    
    a.append(b)

apart()

t = int(input())

for m in range(0, t):
  f = int(input())
  h = int(input())

  print(a[f][h-1])