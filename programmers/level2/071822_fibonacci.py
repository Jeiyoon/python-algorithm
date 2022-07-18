# date: 2022.07.18
# author: jeiyoon

def solution(n: int) -> int:
  # n은 2 이상 100,000 이하인 자연수입니다.
  table = [0] * (n + 1)
  table[2], table[3] = 1, 2

  for idx in range(4, n+1):
    table[idx] = table[idx-1] + table[idx-2]
  
  return table[-1] % 1234567
