# date: 2022.07.04
# author: jeiyoon
import operator
from copy import deepcopy
from typing import List

ops = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul}

def op_calculator(expr_list: List[int], op1: str, op2: str, op3: str) -> int:
  # op1
  pop_list = []
  if op1 in expr_list:
    for idx in range(len(expr_list)):
      if expr_list[idx] == op1:
        expr_list[idx-1] = ops[expr_list[idx]](int(expr_list[idx-1]), int(expr_list[idx+1]))
        expr_list[idx+1] = expr_list[idx-1]
        pop_list.append(idx)
        pop_list.append(idx+1)
    
  expr_list = [expr for idx, expr in enumerate(expr_list) if not idx in pop_list]
  # print(expr_list)

  # op2
  pop_list = []
  if op2 in expr_list:
    for idx in range(len(expr_list)):
      if expr_list[idx] == op2:
        expr_list[idx-1] = ops[expr_list[idx]](int(expr_list[idx-1]), int(expr_list[idx+1]))
        expr_list[idx+1] = expr_list[idx-1]
        pop_list.append(idx)
        pop_list.append(idx+1)
  
  expr_list = [expr for idx, expr in enumerate(expr_list) if not idx in pop_list]
  # print(expr_list)

  # op3
  pop_list = []
  if op3 in expr_list:
    for idx in range(len(expr_list)):
      if expr_list[idx] == op3:
        expr_list[idx-1] = ops[expr_list[idx]](int(expr_list[idx-1]), int(expr_list[idx+1]))
        expr_list[idx+1] = expr_list[idx-1]
        pop_list.append(idx)
        pop_list.append(idx+1)
        # print("expr_list: ", expr_list)
  
  # exception: last operator
  # print("pop_list: ",pop_list)
  expr_list = [expr for expr in expr_list if str(type(expr)) == "<class 'int'>" ]
  # print(max(map(abs,expr_list)))

  return max(map(abs,expr_list))

def solution(expression: str) -> int:
    answer_list = []
    expr_list = []
    
    # 1. split nums and operators
    pointer = 0
    for idx, char in enumerate(expression):
      if not char.isdigit(): # 0 1 2 3
        expr_list.append(expression[pointer:idx])
        expr_list.append(expression[idx])
        pointer = idx + 1
    expr_list.append(expression[pointer:])
    # print("expr_list: ", expr_list)
    # ['100', '-', '200', '*', '300', '-', '500', '+']
    
    # 2. calculate
    # 2 - (1): "+" > "-" > "*"
    answer_list.append(op_calculator(deepcopy(expr_list), "+", "-", "*"))
    # print("1")
    # 2 - (2): "+" > "*" > "-"
    answer_list.append(op_calculator(deepcopy(expr_list), "+", "*", "-"))
    # print("2")
    # 2 - (3): "-" > "+" > "*"
    answer_list.append(op_calculator(deepcopy(expr_list), "-", "+", "*"))
    # print("3")
    # 2 - (4): "-" > "*" > "+"
    answer_list.append(op_calculator(deepcopy(expr_list), "+", "-", "*"))
    # print("4")
    # 2 - (5): "*" > "+" > "-"
    answer_list.append(op_calculator(deepcopy(expr_list), "*", "+", "-"))
    # print("5")
    # 2 - (6): "*" > "-" > "+"
    answer_list.append(op_calculator(deepcopy(expr_list), "*", "-", "+"))
    # print("6")

    return max(answer_list)


# result = 60420
expression = "100-200*300-500+20"

# result = 300
# expression = "50*6-3*2"

print(solution(expression))
