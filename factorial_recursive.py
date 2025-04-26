# function to find fuctorial using recursive
def factorial_recursive(number):
  #base case  to give 1=factorial if n is 0
  if number==0:
    return 1
  else:#recusive part where the number is multiplied by number-1 factorial
    return number*factorial_recursive(number-1)

print(factorial_recursive(4))#output is meant to be 24

    
