# https://projecteuler.net/problem=5

def prime_factors(n):
  prime_factors = []
  divisor = 2
  while n != 1:
    while divisor <= n:
      if n % divisor == 0:
        # the smallest divisor will always be a prime number
        prime_factors.append(divisor)
        n = n // divisor
        break
      divisor += 1
  return prime_factors

def smallest_multiply(n):
  factors = []
  i = 1
  while i <= n:
    factors.append(prime_factors(i))
    i += 1
  return min(factors)
    

print(smallest_multiply(6))
