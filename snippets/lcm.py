def lcm(a1: int, a2: int) -> int:
  result = 0

  for idx in range(a2, (a1 * a2) + 1):
    if idx % a1 == 0 and idx % a2 == 0:
      result = idx
      break

  return result
