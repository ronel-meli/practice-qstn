#function to reversed string
def reverse_string(s):
  #empty string to hold the reversed string
  reversed_str=""
  #loop each character to form the reversed string
  for char in s:
    reversed_str=char+reversed_str #Each character comes to the front of the reversed string
return reversed_str
print(reverse_sting("ronel"))
#ouput= lenor
