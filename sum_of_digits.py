#function to calculate the sum of digits in a number
def sum_of_digits(n)
#initialise the total to 0
total=0
#loop until n becomes 0
while n>0:
  last_digit=n%10 #extracting the last digit by getting the reminder which will be the last digit of the number
total+=last_digit #adds the last digit to 0
n=n//10#removes the last digits and the loop continues with the remaining digits
return total
print(sum_of_digits(12345)) # should give  the sum that is 15

