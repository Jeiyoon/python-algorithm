from typing import List

def sieve_of_eratosthenes(c: int) -> List[int]:
  sieve = [True] * (c + 1)

  for i in range(2, int(c ** 0.5) + 1):
      if sieve[i] == True: # i is a prime number
          for j in range(i + i, c + 1, i):
              sieve[j] = False

  prime_num_list = [i for i in range(2, c + 1) if sieve[i] == True]

  return prime_num_list

c = 50
print(sieve_of_eratosthenes(c))
