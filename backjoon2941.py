import re

s = input()
p = 'c=|c-|dz=|d-|lj|nj|s=|z='

c = re.findall(p, s)

for i in c:
  s = s.replace(i, '!', 1)

print(len(s))