def cal(f):
  if ord(f) <= 79:
    a = (ord(f) - 65) // 3 + 3
  elif ord(f) > 79 and ord(f) <= 83:
    a = 8
  else:
    a = (ord(f) - 84) // 3 + 9

  if a > 10:
    return 10
  return a

n = input()

result = 0
for i in n:
  result += cal(i)
print(result)