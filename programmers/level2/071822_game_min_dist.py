# date: 2022.07.18
# author: jeiyoon
"""
maps is a 2-dimensional array containing the status of the game map with n x m size. n and m are natural number between 1 and 100.

n and m may be either the same or different each other, 

but there is no case where both are given as 1.

maps consists of 0 and 1 only, which indicates the space with wall and without wall, respectively.

Initially, the character is located at the left top of the game map (1, 1), and the camp of the other team is at the right bottom of the game map (n, m).
"""
from typing import List

def solution(maps: List[List[int]]) -> int:
  answer = 0

  x_coordinate = len(maps) - 1 # 5
  y_coordinate = len(maps[0]) - 1 # 5
  print(x_coordinate)

  while x_coordinate != 0 and y_coordinate != 0:
    print("####################################")
    print("x_coordinate: ", x_coordinate)
    print("y_coordinate: ", y_coordinate)
    # 1. check current position
    dir_list = []
    # left
    if y_coordinate > 0:
      dir_list.append('left')
    # up
    if x_coordinate > 0:
      dir_list.append('up')
    # right
    if y_coordinate < 4:
      dir_list.append('right')
    # down
    if x_coordinate < 4:
      dir_list.append('down')

    print("dir_list: ", dir_list)

    # 2. check whether wall or road
    # left
    if 'left' in dir_list:
      if maps[x_coordinate][y_coordinate - 1] == 0:
        dir_list.remove('left')
    # up
    if 'up' in dir_list:
      if maps[x_coordinate - 1][y_coordinate] == 0:
        dir_list.remove('up')
    # right
    if 'right' in dir_list:
      if maps[x_coordinate][y_coordinate + 1] == 0:
        dir_list.remove('right')
    # down
    if 'down' in dir_list:
      if maps[x_coordinate + 1][y_coordinate] == 0:
        dir_list.remove('down')

    print("dir_list: ", dir_list)
    
    # 3. if there's no road, return -1
    if len(dir_list) == 0:
      return -1

    # 4. go with "left" and "up" priority 
    if 'left' in dir_list:
      y_coordinate -= 1
      answer += 1
      continue
    if 'up' in dir_list:
      x_coordinate -= 1
      answer += 1
      continue
    if 'down' in dir_list:
      y_coordinate += 1
      answer += 1
      continue
    if 'right' in dir_list:
      x_coordinate += 1
      answer += 1
      continue
    
  return answer

# result = 11
maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]

# result = -1
# maps = [[1,0,1,1,1],
#         [1,0,1,0,1],
#         [1,0,1,1,1],
#         [1,1,1,0,0],
#         [0,0,0,0,1]]


print(solution(maps))
