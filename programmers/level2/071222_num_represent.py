# date: 2022.07.12
# author: jeiyoon
def solution(n):
  answer = 0

  for i in range(1, n + 1):
    temp = i

    for j in range(i + 1, n + 1):
      temp += j
      
      if temp > n:
        break
      
      if temp == n:
        answer += 1
        break

  if temp == n:
    answer += 1

  return answer

# result = 4
n = 15
print(solution(n))
