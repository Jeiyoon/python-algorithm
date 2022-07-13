# date: 2022.07.13
# author: jeiyoon
# https://www.daleseo.com/python-global-nonlocal/
from typing import List

def solution(numbers: List[int], target: int) -> int:
  answer = 0
  idx = 0
  result = 0

  def dfs(idx: int, sign: int, result: int) -> None:
    nonlocal answer
    
    if idx == len(numbers):
        if result == target:
            answer = answer + 1
        return

    result = result + (numbers[idx] * sign)
    
    dfs(idx + 1,  1, result)
    dfs(idx + 1, -1, result)

  dfs(idx, -1, result)
  dfs(idx, 1, result)
      
  return int(answer / 2)


# return 5
numbers = [1, 1, 1, 1, 1]
target = 3

# return 2
# numbers = [4, 1, 2, 1]
# target = 4

print(solution(numbers, target))
