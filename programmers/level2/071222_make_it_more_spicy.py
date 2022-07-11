# date: 2022.07.12
# author: jeiyoon
"""
효율성 테스트 탈락
"""
from typing import List
from collections import deque

def solution(scoville: List[int], K: int) -> int:
  done = False
  count = 0

  while not done:
    # 1. all food >= K
    check = [k for k in scoville if k >= K]
    
    if len(check) != len(scoville):
      if len(scoville) == 1: # impossible
        return -1
      
      count += 1
      # 2. find min and second-min values
      temp = deque(sorted(scoville))
      min_val = temp.popleft()
      second_min_val = temp.popleft()
      
      # 3. new food
      new_val = min_val + (second_min_val * 2)

      scoville.pop(scoville.index(min_val))
      scoville.pop(scoville.index(second_min_val))
      
      scoville.append(new_val)    

    else: # all food are bigger than K
      done = True

  return count

# return = 2
scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))
