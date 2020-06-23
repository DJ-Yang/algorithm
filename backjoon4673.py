def solo_num(n, a):
  s = str(n)
  
  for i in s:
    n += int(i)
  if n <= 10000:
    if n in a:
      a.pop(a.index(n))
      solo_num(n, a)
  return

result = []

for i in range(1, 10001):
  result.append(i)

for i in result:
  if i in result:
    solo_num(i, result)

for i in result:
  print(i)
