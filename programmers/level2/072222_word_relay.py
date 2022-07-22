# date: 2022.07.22
# author: jeiyoon
from typing import List

def solution(n: int, words: List[str]) -> List[int]:
  # The number of participants in the word relay "n" is a natural number between 2 and 10.
  # The length of the words is between 2 and 50.
  # "words" is an array containing words said in the word relay and its length is more than "n" and less than 100.
  
  # If there is no dropout with the given words, return [0, 0].
  appeared_words = []

  # (1) appeared words
  for idx, word in enumerate(words):
    if len(appeared_words) == 0:
      appeared_words.append(word)
      continue

    if word in appeared_words:
      return [(idx % n) + 1, (idx // n) + 1]

    appeared_words.append(word)

  # (2) no relayed word
  for idx in range(len(words)):
    if idx == 0:
      continue
    
    if words[idx-1][-1] != words[idx][0]:
      return [(idx % n) + 1, (idx // n) + 1]

  # Return an answer in [ number, turn ] format.
  return [0, 0]


n_list = [3, 5, 2]
words_list = [["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"],  # [3, 3]
              ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"], # [0, 0]
              ["hello", "one", "even", "never", "now", "world", "draw"], # [1, 3]
              ]

for n, words in zip(n_list, words_list):
  print(solution(n, words))
