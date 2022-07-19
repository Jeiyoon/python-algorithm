# date: 2022.07.19
# author: jeiyoon
from typing import List, Dict, Union
from collections import defaultdict
from math import ceil

def solution(fees: List[int], records: List[Union[str, int]]) -> List[int]:
  # 잘못된 시각("25:22", "09:65" 등)은 입력으로 주어지지 않습니다.
  # 마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않습니다.
  # 주차장에 없는 차량이 출차되는 경우는 주어지지 않습니다.
  answer = []
  records_dict = defaultdict(Dict)
  fees_dict = defaultdict(int)

  for record in records:
    record = record.split()
    time = record[0].split(":")
    minute = int(time[0])*60 + int(time[1])
    
    # 주차장에 이미 있는 차량(차량번호가 같은 차량)이 다시 입차되는 경우는 주어지지 않습니다.
    if record[2] == 'IN':
      records_dict[record[1]] = minute
    else: # 'OUT'
      parking_time = minute - records_dict[record[1]]
      fees_dict[record[1]] = fees_dict[record[1]] + parking_time
    
      del records_dict[record[1]]

  # leftover
  for key in records_dict.keys():
    time = "23:59".split(":")
    minute = int(time[0])*60 + int(time[1])

    parking_time = minute - records_dict[key]
    fees_dict[key] = fees_dict[key] + parking_time
  
  # paying fee
  for key in sorted(fees_dict):
    if fees_dict[key] <= fees[0]:
        answer.append(fees[1])
    else: # parking_time > fees[0]
      answer.append(fees[1] + int(ceil((fees_dict[key] - fees[0]) / fees[2]) * fees[3]))
  return answer

# fees[0] = 기본 시간(분)
# fees[1] = 기본 요금(원)
# fees[2] = 단위 시간(분)
# fees[3] = 단위 요금(원)
fees_list = [[180, 5000, 10, 600], # [14600, 34400, 5000]
             [120, 0, 60, 591], # [0, 591] 
             [1, 461, 1, 10]] # [14841]

records_list = [["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
                ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"],
                ["00:00 1234 IN"]]


for fees, records in zip(fees_list, records_list):
  print(solution(fees, records))
