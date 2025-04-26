#create function to calculate sum of numbers on a list
def calculate_sum(numbers):
  #start total to 0
  sum=O
  #for loop for the numbers of the list
for num in numbers:
  sum+=num # add each number of the list to the sum
  return sum

print(calculate_sum([5,6,7,8]))
#output should be 26
  
