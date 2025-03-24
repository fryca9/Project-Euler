def largest_prime_factor(n):
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
  return max(prime_factors)

print(largest_prime_factor(600851475143))
