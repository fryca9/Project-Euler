# https://projecteuler.net/problem=5

def is_prime(n):
  if n < 2:
    return False
  
  divisor = 2
  while divisor**2 <= n:
    if n % divisor == 0:
      return False
    divisor += 1
  return True

def get_prime_factors(n):
  factors = []
  divisor = 2
  while n != 1:
    while divisor <= n:
      if is_prime(divisor) and n % divisor == 0:
        # the smallest divisor will always be a prime number
        factors.append(divisor)
        n //= divisor
        break
      divisor += 1
  return factors

def smallest_multiply(n):
  # Get prime factors for all numbers from 1 to n
  all_factors = [get_prime_factors(i) for i in range(2, n+1)]
  unique_factors = [num for num in range(2, n+1) if is_prime(num)]
  max_exponents = []
  
  # Find the maximum exponent for each prime
  for prime in unique_factors:
    max_exponent = max(factors.count(prime) for factors in all_factors)
    max_exponents.append(max_exponent)
  
  # Calculate the least common multiple
  factors = {k: v for k,v in zip(unique_factors, max_exponents)}
  result = 1
  for k,v in factors.items():
    result *= k**v
  return result 
    

print(smallest_multiply(20))
