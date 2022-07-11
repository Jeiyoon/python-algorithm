# date: 2022.07.11
# author: jeiyoon
# 다음에 비슷한 문제가 출제될때는 알고리즘이 주어지지 않을수도 있을듯
from collections import Counter

def check_correctness(w: str) -> bool:
  stack = []
  
  for w_char in w:
    if w_char == '(':
      stack.append(w_char)
    else: # ')'
      if len(stack) == 0:
        continue
      else: # '(' in the stack
        stack.pop()

  if len(stack) == 0:
    return True
  else:
    return False

def solution(p: str) -> str:
  # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
  if len(p) == 0:
    return p
  
  # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
  # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
  
  # e.g., "()))((()"
  # u = "()"
  # v = "))((()"
  # 문자열 u가 "올바른 괄호 문자열"이므로 그대로 두고, v에 대해 재귀적으로 수행합니다.
  # 다시 두 문자열 u, v로 분리합니다

  # 다시 두 문자열 u, v로 분리합니다.
  # u = "))(("
  # v = "()"
  
  # u가 "올바른 괄호 문자열"이 아니므로 다음과 같이 새로운 문자열을 만듭니다.
  # v에 대해 1단계부터 재귀적으로 수행하면 "()"이 반환됩니다.
  # u의 앞뒤 문자를 제거하고, 나머지 문자의 괄호 방향을 뒤집으면 "()"이 됩니다.
  # 따라서 생성되는 문자열은 "(" + "()" + ")" + "()"이며, 최종적으로 "(())()"를 반환합니다.
  # 처음에 그대로 둔 문자열에 반환된 문자열을 이어 붙이면 "()" + "(())()" = "()(())()"가 됩니다.
  p_stack = []

  for idx, p_char in enumerate(p):
    p_stack.append(p_char)
    left_num = Counter(p_stack)['('] # of (
    right_num = Counter(p_stack)[')'] # of )
    
    if left_num == right_num:
      u = p[:idx + 1]
      v = p[idx + 1:]
      # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
      if check_correctness(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        result = u + solution(v)
        break
      
      # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
      else: # u is not correct
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        temp = "" + "("
        # print("temp1: ", temp)
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        temp += solution(v)
        # print("temp2: ", temp)
        # 4-3. ')'를 다시 붙입니다.
        temp += ")"  
        # print("temp3: ", temp)
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        # ')' -> '('
        # '(' -> ')'
        u = u[1:len(u)-1]
        u = list(u)
        for idx in range(len(u)):
          if u[idx] == '(':
            u[idx] = ')'
          else: # u[idx] == ')'
            u[idx] = '('
        u = "".join(u)
        temp += u
        # 4-5. 생성된 문자열을 반환합니다.
        result = temp
        break

  return result

# result = "(()())()"
# p = "(()())()"

# result = 	"()"
# p = ")("

result = "()(())()"
p = "()))((()"

answer = solution(p)

print("################################")
print("result: \t", result)
print("solution(p): \t", answer)
print("result == solution(p): ", result == answer)
print("################################")
