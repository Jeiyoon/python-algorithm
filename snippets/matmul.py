# if matmul is feasible
from typing import List

def solution(arr1:List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
  answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

  for i in range(len(arr1)):
    for j in range(len(arr2[0])):
      temp = 0
      
      for a1, a2 in zip(arr1[i], [a[j] for a in arr2]):
        temp += a1* a2

      answer[i][j] += temp
        
  return answer
