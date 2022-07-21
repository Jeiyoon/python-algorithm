# date: 2022.07.21
# author: jeiyoon
from collections import deque

def solution(s: str) -> bool:
  # Length of string s: natural number less than 100,000
  stack = []
  s = deque(s)

  while len(s) > 0:
    char = s.popleft()

    if char == '(':
      stack.append(char)
    else: # ')'
      if len(stack) == 0:
        return False
      stack.pop()

  if len(stack) > 0:
    return False

  return True

s_list = ["()()",  # True
          "(())()",  # True
          ")()(",  # False
          "(()("]  # False

for s in s_list:
  print(solution(s))
