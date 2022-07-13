# date: 2022.07.13
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
