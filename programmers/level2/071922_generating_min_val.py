# date: 2022.07.19
# author: jeiyoon
from typing import List

def solution(A: List[int],B: List[int]) -> int:
  # Length of array "A" and "B" : natural number less than 1,000.
  # Each element of array "A" and "B" : natural number less than 1,000.
  answer = 0

  # "A" and "B" that have the same length. 
  A = sorted(A)
  B = sorted(B, reverse=True)

  for a, b in zip(A, B):
    answer += a*b

  return answer

# result = 29
A = [1, 4, 2]  # 1 - 4 - 2
B = [5, 4, 4]  # 5 - 4 - 4

# result = 10
# A = [1,2]  # 1 - 2 
# B = [3,4]  # 4 - 3

print(solution(A, B))
