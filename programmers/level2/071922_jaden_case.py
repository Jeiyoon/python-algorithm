# date: 2022.07.19
# author: jeiyoon
def solution(s: str) -> str:
  answer = ''
  s = list(s.lower())
  cnt = 0

  for idx in range(len(s)):
    if cnt == 0:
      s[idx] = s[idx].upper()
    if s[idx] == " ":
      cnt = 0
      continue
    cnt += 1

  return "".join(s)

# return = "3people Unfollowed Me"
s = "3people unFollowed me"	

# return = "For The Last Week"
# s = "for the last week"

print(solution(s))
