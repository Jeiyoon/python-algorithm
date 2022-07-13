# date: 2022.07.14
# author: jeiyoon
# time out
def solution(n: int) -> int:
  answer = 0
  idx = 0
  result = 0

  def dfs(idx: int, jump: int, result: int) -> None:
    nonlocal answer
    if idx <= n:
      if result == n:
        answer += 1
    if idx > n:
      return
    
    result += jump
    dfs(idx + 1, 1, result)
    dfs(idx + 1, 2, result)
    

  dfs(idx, 1, result)
  dfs(idx, 2, result)
  
  answer /= 2 
  return int(answer % 1234567)

# result = 5
# n = 4

# result = 3
n = 3

print(solution(n))


"""
-time out

from itertools import combinations

def solution(n: int) -> int:
  # x + 2y = n
  # n은 1 이상, 2000 이하인 정수입니다.
  if n == 1:
    return 1

  answers = []
  max_y = 0
  result = 0

  # 1. find y
  for i in range(n):
    if (2 * i) > n:
      max_y = i - 1
      break
  
  print(max_y)

  # 2. find all (x, y)
  for y in range(max_y + 1):
    x = n - 2 * y
    answers.append([x, y])

  # 3. find answer
  for answer in answers:
    temp = [1] * answer[0] + [2] * answer[1]
    result += len(list(combinations(temp, answer[0])))
"""
