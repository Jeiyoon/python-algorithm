# date: 2022.07.20
# author: jeiyoon
from typing import List

def solution(arr1:List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
  # 곱할 수 있는 배열만 주어집니다.
  # 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
  # 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
  """
  answer = [[] * len(arr2)] * len(arr1) 
  이런식으로 선언하면 얕은 복사라 곱해서 생성한 애들끼리 다 똑같은 값이 들어감
  """
  answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]

  for i in range(len(arr1)):
    for j in range(len(arr2[0])):
      temp = 0
      
      for a1, a2 in zip(arr1[i], [a[j] for a in arr2]):
        temp += a1* a2

      answer[i][j] += temp
        
  return answer

# return = [[15, 15], [15, 15], [15, 15]]
# arr1 = [[1, 4], 
#         [3, 2], 
#         [4, 1]]
# arr2 = [[3, 3], 
#         [3, 3]]

# return = [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
arr1 = [[2, 3, 2], 
        [4, 2, 4], 
        [3, 1, 4]]	
arr2 = [[5, 4, 3], 
        [2, 4, 1], 
        [3, 1, 1]]

# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]  # 3 * 3
# arr2 = [[5, 4], [2, 4], [3, 1]]  # 3 * 2

print(solution(arr1, arr2))
