# date: 2022.07.14
# author: jeiyoon
# https://smlee729.github.io/python/algorithm/2015/03/14/1-number-of-solutions.html
# https://kin.naver.com/qna/detail.naver?d1id=11&dirId=11040302&docId=354970113&qb=7KSR67O17KGw7ZWpIOqzhOyImA==&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0
from typing import Dict

def find_solution(n: int, k: int, cache = dict()):
  if k == 0:
    cache[(n, k)] = 0
    return 0
  if k == 1 and n != 0:
    cache[(n, k)] = 1
    return 1
  
  if (n, k) in cache:
    return cache[(n, k)]
  
  count = 0

  for idx in range(n + 1): # 0 1 2 3 4
    print("n: {}, k: {}".format(n, k))
    count += find_solution(n - idx, k - 1, cache)
    print("count: ", count)

  cache[(n, k)] = count
  print("cache: ", cache)

  return count

def solution(n: int) -> int:
  # x + 2y = n (1 <= n <= 2000)
  # 1. exception: n == 1
  if n == 1:
    return 1
  
  # 2. whether n is odd or even
  if n % 2 == 0: # even
    # x is even
    # x == 2t
    # t + y = n/2
    n = int(n / 2)
  else: # odd
    # x is odd
    # x == 2t + 1
    # t + y = (n-1)/2
    n = int((n - 1) / 2)  

  print("n: ", n)
  # 3. t + y = n' -> Dynamic Programming
  # here, # of term 'k' is two
  k = 2
  return find_solution(n, k)

# result = 5
n = 4

# result = 3
# n = 3

print(solution(n))
