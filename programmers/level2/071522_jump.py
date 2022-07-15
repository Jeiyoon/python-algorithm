# date: 2022.07.15
# author: jeiyoon
# timeout
# https://smlee729.github.io/python/algorithm/2015/03/14/1-number-of-solutions.html
# https://kin.naver.com/qna/detail.naver?d1id=11&dirId=11040302&docId=354970113&qb=7KSR67O17KGw7ZWpIOqzhOyImA==&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0
from typing import Dict
from itertools import combinations

def find_solution(N: int, n: int, k: int, cache = dict()): 
  if k == 0:
    return 0

  if k == 1:
    t = n
    y = N - n
    temp = []
    # print("(x, y): {}".format((t, y * 2)))
    temp.extend(['x'] * t)
       
    if N % 2 == 0:  
      temp.extend(['y'] * (y * 2))
    else:
      temp.extend(['y'] * (y * 2 + 1))
    
    # print("temp: ", temp)
    # print("len: ", len(list(combinations(temp, t))))
      
    return len(list(combinations(temp, t))) # 1

  if (n, k) in cache:
    return cache[(n, k)]
  
  count = 0
  
  for idx in range(n + 1): # 0 1 2
    # print("n: {}, k: {}".format(n, k))
    count += find_solution(N, n - idx, k - 1, cache)
    # print("count: ", count)

  cache[(n, k)] = count
  # print("cache: ", cache)

  return count

def solution(n: int) -> int:
  # 2x + y = n (1 <= n <= 2000)
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

  # print("n: ", n)
  # 3. t + y = n' -> Dynamic Programming
  # here, # of term 'k' is two
  k = 2
  N = n # max(n) for y
  return find_solution(N, n, k) % 1234567

# result = 5
# n = 4

# result = 3
n = 3

print(solution(n))
