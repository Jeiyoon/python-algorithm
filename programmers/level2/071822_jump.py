# date: 2022.07.18
# author: jeiyoon
"""
these links are not related to this problem but they are worth reading 
  https://smlee729.github.io/python/algorithm/2015/03/14/1-number-of-solutions.html
  https://kin.naver.com/qna/detail.naver?d1id=11&dirId=11040302&docId=354970113&qb=7KSR67O17KGw7ZWpIOqzhOyImA==&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0
"""
def solution(n: int) -> int:
  # n은 1 이상, 2000 이하인 정수입니다. 
  if n == 1: # table[0]
    return 1

  table = [0] * (n + 1)
  table[1], table[2] = 1, 2

  for idx in range(3, n+1):
    table[idx] = table[idx-1] + table[idx-2]
  
  return table[-1] % 1234567

# result = 5
n = 4

# result = 3
# n = 3

print(solution(n))
