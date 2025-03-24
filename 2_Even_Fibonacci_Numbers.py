# https://projecteuler.net/problem=2

def fibonacci_num(n):
  if n <= 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    return fibonacci_num(n-1) + fibonacci_num(n-2)

def fibo_even_sum(n):
  result = 0
  a = 1
  b = 1
  z = 0
  
  # that is the quickest way -> you do not need to use fibonacci_num()
  while z < n:
    z = a + b
    if z % 2 == 0:
      result += z
    a = b
    b = z
  return result

print(fibo_even_sum(4000000))
