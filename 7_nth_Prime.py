# https://projecteuler.net/problem=7

def is_prime(n):
  if n < 2:
    return False
  divisor = 2
  while divisor**2 <= n:
    if n % divisor == 0:
      return False
    divisor += 1
  return True

def nth_prime(n):
  num = 2
  numbers_left = n
  while numbers_left > 0:
    if is_prime(num):
      numbers_left -= 1
    if numbers_left != 0:
      num += 1
  return num

print(nth_prime(10001))
