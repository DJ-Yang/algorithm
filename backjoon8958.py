t = int(input())

result = 0

def check_score(array, i, score):
  score = score
  if i >= 0:
    if array[i] == 'O':
      score += 1
      score = check_score(q, i-1, score)
      return int(score)
    else:
      return int(score)
  else:
    return score

for i in range(1, t + 1):
  q = input()

  for i in range(0, len(q)):
    score = 0
    if q[i] == 'X':
      continue
    else:
      score += 1
      score = check_score(q, i-1, score)
    result += score
  print(result)
  result = 0