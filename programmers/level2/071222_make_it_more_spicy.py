# date: 2022.07.12
# author: jeiyoon
from typing import List
import heapq

def solution(scoville: List[int], K: int) -> int:
  done = False
  count = 0  
  scoville.sort()
  heapq.heapify(scoville)

  while not done:
    # end condition: 1
    if scoville[0] >= K:
      done = True
      continue

    # end condition: 2
    if len(scoville) == 1 and scoville[0] < K:
      return -1
    
    min_val = heapq.heappop(scoville)
    second_min_val =heapq.heappop(scoville)
    new_val = min_val + (second_min_val * 2)
    heapq.heappush(scoville, new_val)

    count += 1

  return count

# return = 2
scoville = [1, 3, 2, 9, 10, 12]
K = 7

print(solution(scoville, K))
