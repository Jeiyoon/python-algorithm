# date: 2022.07.13
# author: jeiyoon
# 타임 아웃
from typing import List
from itertools import permutations
from copy import deepcopy

def solution(numbers: List[int], target: int) -> int:
  answer = []
  temp = []
  minus_and_plus_list = [n for n in range(len(numbers))]
  # print(minus_and_plus_list)
  
  for minus_num in range(len(numbers) + 1): # # of minus
    # print("################################")
    # print("minus_num: ", minus_num)
    # print("################################")
    for indices in list(permutations(minus_and_plus_list, minus_num)): # each permutation
      temp = deepcopy(numbers)
      # print("indices: ", indices)
      for idx in indices:
        # print("idx: ", idx)
        temp[idx] = -temp[idx]
        # print("temp: ", temp)
      if sum(temp) == target:
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$HERE")
        if temp not in answer:
          answer.append(temp)
  
  # print("answer: ", answer)
  return len(answer)


# return 5
numbers = [1, 1, 1, 1, 1]
target = 3

# return 2
# numbers = [4, 1, 2, 1]
# target = 4

print(solution(numbers, target))
