# date: 2022.07.19
# author: jeiyoon
from typing import List
from collections import deque

def lcm(a1: int, a2: int) -> int:
  result = 0

  for idx in range(a2, (a1 * a2) + 1):
    if idx % a1 == 0 and idx % a2 == 0:
      result = idx
      break

  return result

def solution(arr: List[int]) -> int:
  # arr은 길이 1이상, 15이하인 배열입니다.
  # arr의 원소는 100 이하인 자연수입니다.
  arr = deque(sorted(arr))

  while len(arr) >= 2:
    a1 = arr.popleft()
    a2 = arr.popleft()
    if a1 > a2:
      arr.append(lcm(a2, a1))
    else:
      arr.append(lcm(a1, a2))
  
  return arr[-1]

# result = 168
arr = [2,6,8,14]

# result = 6
# arr = [1,2,3]

# result = 144
# arr = [3,4,9,16]

# result = 12
# arr = [4,3,2]


print(solution(arr))
