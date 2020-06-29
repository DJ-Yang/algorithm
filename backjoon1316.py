t = int(input())

count = 0

for x in range(0, t):
  s = input()
  i = 0
  a = []
  check = True

  while i < len(s):
    jump = 1
    try:
      while s[i] == s[i+jump]:
        jump += 1
    except IndexError:
      pass
    a.append(s[i])

    i = i + jump

  for n in range(0, len(a)):
    if not a.count(a[n]) == 1:
      check = False

  if check:
    count += 1

print(count)