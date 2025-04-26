#fucntion to compute the factorial using a loop
def compute_factorial(number):
  result=1 #because any no multiplied by 0 will be 0 hence we should multiply the subsequent numbers by 1
#loop
for i in range(1,number+1):#multiply 1 by every number from 1 to the number
  result*= i
  return result

print(compute_factorial(4))
  #output should be 24

  
