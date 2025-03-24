# https://projecteuler.net/problem=1

def sum_of_multiples(a=3, b=5, N=1000):
  N -= 1  # the sum must be of numbers below N
  # simple math -> formula for the sum of arithmetic sequence
  num_of_terms_a = N // a
  sum_a = (num_of_terms_a / 2)*(2*a + (num_of_terms_a - 1)*a)
  num_of_terms_b = N // b
  sum_b = (num_of_terms_b / 2)*(2*b + (num_of_terms_b - 1)*b)
  # we need to subtract the repeating terms
  num_of_terms_ab = N // (a*b)
  sum_ab = (num_of_terms_ab / 2)*(2*a*b + (num_of_terms_ab - 1)*a*b)
  return int(sum_a + sum_b - sum_ab)

print(sum_of_multiples(3, 5, 1000))
