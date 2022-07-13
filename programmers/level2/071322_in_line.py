# date: 2022.07.13
# author: jeiyoon
from typing import List
from math import factorial

def solution(n: int, k: int) -> List[int]:
  result = []
  
  def recursion(n_list: List[int], k: int) -> int:
    nonlocal result

    if len(n_list) == 1:
      result.append(n_list[0])
      return

    gap = factorial(len(n_list) - 1)
    
    for idx in range(len(n_list)):
      if gap * idx < k and k <= gap * (idx + 1):
        result.append(n_list[idx])
        n_list.remove(n_list[idx])
        recursion(n_list, k - (idx * gap)) 

  answer = [i+1 for i in range(n)]
  recursion(answer, k)

  return result

# result = [3, 1, 2]
n = 3
k = 5

print(solution(n, k))
