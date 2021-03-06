# date: 2022.07.05
# author: jeiyoon
import operator
from copy import deepcopy
from typing import List

ops = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul}

def op_calculator(expr_list: List[int], op1: str, op2: str, op3: str) -> int:
  # op1
  while op1 in expr_list:
    for idx in range(len(expr_list)):
      if expr_list[idx] == op1:
        right = expr_list.pop(idx+1)
        left = expr_list.pop(idx-1)
        expr_list[idx-1] = ops[op1](int(left), int(right))
        break        

  # op2
  while op2 in expr_list:
    for idx in range(len(expr_list)):
      if expr_list[idx] == op2:
        right = expr_list.pop(idx+1)
        left = expr_list.pop(idx-1)
        expr_list[idx-1] = ops[op2](int(left), int(right))
        break        

  # op3
  while op3 in expr_list:
    for idx in range(len(expr_list)):
      if expr_list[idx] == op3:
        right = expr_list.pop(idx+1)
        left = expr_list.pop(idx-1)
        expr_list[idx-1] = ops[op3](int(left), int(right))
        break        

  return abs(expr_list[-1])

def solution(expression: str) -> int:
    answer_list = []
    expr_list = []
    
    # 1. split nums and operators
    pointer = 0
    for idx, char in enumerate(expression):
      if not char.isdigit(): 
        expr_list.append(expression[pointer:idx])
        expr_list.append(expression[idx])
        pointer = idx + 1
    expr_list.append(expression[pointer:])
   
    # 2. calculate
    # 2 - (1): "+" > "-" > "*"
    answer_list.append(op_calculator(deepcopy(expr_list), "+", "-", "*"))
    # # 2 - (2): "+" > "*" > "-"
    answer_list.append(op_calculator(deepcopy(expr_list), "+", "*", "-"))
    # # 2 - (3): "-" > "+" > "*"
    answer_list.append(op_calculator(deepcopy(expr_list), "-", "+", "*"))
    # # 2 - (4): "-" > "*" > "+"
    answer_list.append(op_calculator(deepcopy(expr_list), "-", "*", "+"))
    # # 2 - (5): "*" > "+" > "-"
    answer_list.append(op_calculator(deepcopy(expr_list), "*", "+", "-"))
    # # 2 - (6): "*" > "-" > "+"
    answer_list.append(op_calculator(deepcopy(expr_list), "*", "-", "+"))

    return max(answer_list)

# result = 60420
expression = "100-200*300-500+20"
# expression = "1-1"

# result = 300
# expression = "50*6-3*2"

print(solution(expression))
