# date: 2022.07.12
# author: jeiyoon

def solution(s: str) -> int:
  # exception: odd num
  if len(s) % 2 == 1:
    return 0

  # Length of string : natural number less than 1,000,000.
  s = list(s)
  stack = []

  for char in s:
    if len(stack) >= 1 and stack[-1] == char:
      stack.pop()
    else:
      stack.append(char)        

  if len(stack) == 0:
    return 1
  else:
    return 0

# result = 1
s = 'baabaa'
# s = 'aaaabaabaaaaaa'

# result = 0
# s = 'cdcdcdcdcdcdcdcdcdcdcdcd'
# s = "a"

print(solution(s))
