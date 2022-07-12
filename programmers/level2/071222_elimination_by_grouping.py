# date: 2022.07.12
# author: jeiyoon
# 타임아웃
from copy import deepcopy

def solution(s: str) -> int:
  s = list(s)
  
  while len(s) != 0: 
    # print("s: ", s)
    before_s = deepcopy(s)

    for idx in range(len(s) - 1):
      if s[idx] == s[idx + 1]:
        s.pop(idx)
        s.pop(idx)
        break
    
    if before_s == s:
      return 0

  return 1

# result = 1
# s = 'baabaa'

# result = 0
s = 'cdcd'

print(solution(s))
