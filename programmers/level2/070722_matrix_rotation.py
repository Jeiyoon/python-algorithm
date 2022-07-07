# date: 2022.07.07
# author: jeiyoon
# https://velog.io/@sjy5386/Python-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0
from typing import List

def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:
  # row: vertical, col: horizontal
  answer = []

  # 1. (rows x cols) matrix
  matrix = [[j + (columns * i) for j in range(1, columns + 1)] for i in range(0, rows)]
  
  # 2. rotation
  for query in queries:
    answer_candidate = []
    x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
    mini_row = x2 - x1 + 1 
    mini_col = y2 - y1 + 1 
  
    done = False
    phase = 1
    up_right_block = matrix[x1][y2]

    while not done:  
      # phase 1: →
      if phase == 1:
        for idx in range(mini_col - 1): 
          matrix[x1][y2 - idx] = matrix[x1][y2 - idx - 1]
        phase = 2

      # phase 2: ↑
      if phase == 2:
        for idx in range(mini_row - 1):
          matrix[x1 + idx][y1] = matrix[x1 + idx + 1][y1]
        phase = 3

      # phase 3: ←
      if phase == 3:
        for idx in range(mini_col - 1):  
          matrix[x2][y1 + idx] = matrix[x2][y1 + idx + 1]
        phase = 4

      # phase 4: ↓
      if phase == 4:
        for idx in range(mini_row - 1):
          matrix[x2 - idx][y2] = matrix[x2 - idx - 1][y2]
        # exception
        matrix[x1 + 1][y2] = up_right_block

      done = True
    
    # 3. min number
    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        # exception: central hole
        if x == x1 or x == x2:
          answer_candidate.append(matrix[x][y])
        else: 
          if y == y1 or y == y2: 
            answer_candidate.append(matrix[x][y])
          else:
            pass
    answer.append(min(answer_candidate))

  return answer

# # result = [8, 10, 25]
# rows = 6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

# result = [1, 1, 5, 3]
rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

# # result = [1]
# rows = 100
# columns = 97
# queries = [[1,1,100,97]]

print(solution(rows, columns, queries))
