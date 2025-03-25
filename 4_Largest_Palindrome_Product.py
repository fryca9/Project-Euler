# https://projecteuler.net/problem=4

def is_palindrome(num):
  num = str(num)
  first = num[:len(num) // 2]
  # extract the second half and reverse the order
  second = num[((len(num) + 1) // 2):][::-1] 
  return first == second

def largest_palindrome_product(n):
  max_range = int(str(9)*n)
  min_range = int(str(9) + str(0)*(n-1))
  for i in range(max_range,min_range,-1):
    for j in range(max_range,min_range,-1):
      if is_palindrome(i*j):
        return i*j
  return None

print(palindrome_product(5))
