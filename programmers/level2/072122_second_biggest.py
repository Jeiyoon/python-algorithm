# date: 2022.07.21
# author: jeiyoon
from collections import Counter

def solution(n: int) -> int:
  # n은 1,000,000 이하의 자연수 입니다.
  answer = 0
  
  n_bin = bin(n)[2:]

  count = Counter(n_bin)['1']
  flag = True

  while flag:
    n += 1
    new_n_bin = bin(n)[2:]
    new_count = Counter(new_n_bin)['1']

    if new_count == count:
      answer = n
      flag = False

  return answer

# result = 83
n = 78

# result = 23
# n = 15

print(solution(n))
