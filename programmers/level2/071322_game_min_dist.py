# date: 2022.07.13
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
  return answer

# result = 	11
maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]

# result = 	-1
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]


print(solution(maps))
