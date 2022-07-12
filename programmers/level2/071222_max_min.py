# date: 2022.07.12
# author: jeiyoon
def solution(s: str) -> str:
  s = list(map(int, s.split(" ")))

  return str(min(s)) + " " + str(max(s))

# return "1 4"
# s = "1 2 3 4"

# return "-4 -1"
# s = "-1 -2 -3 -4"

# return "-1 -1"
s = "-1 -1"

print(solution(s))
