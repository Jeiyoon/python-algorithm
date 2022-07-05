# date: 2022.07.06
# author: jeiyoon
from typing import List

def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:
  # https://velog.io/@sjy5386/Python-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0
  # row: vertical
  # col: horizontal
  answer = []

  """
  1. 2차원 배열 선언
  2. 회전 결과가 그 다음 쿼리에 영향을 미침 -> 회전 알고리즘
  3. 가운데 구멍 탐지
  4. 가운데 구멍에 있는 숫자 제외
  """
  # 1. (rows x cols) matrix
  matrix = [[j+i+1 for j in range(columns)] for i in range(0, rows * rows, rows)]

  # 2. rotation
  for query in queries:
    x1, y1, x2, y2 = query
    

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
