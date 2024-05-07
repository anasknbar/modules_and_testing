from itertools import cycle,islice


''' main function'''
def main():
  pass

''' factorial function that use for loop to return the factorial number of n'''
def factorial_iterative(n):
  if n < 0 :
    raise ValueError('Enter positive number') 
  elif n == 0 :
    return 1
  else:
    factoral = 1
    for i in range(n,1,-1):
      factoral *= i
    return factoral


''' factorial function that use recursion  to return the factorial number of n'''
def factorial_recursion(n):
  if n < 0 :
    raise ValueError('Enter positive number') 
  elif n == 0 :
    return 1
  else:
    return n * factorial_recursion(n-1)







 

if __name__ == '__main__':
  main()