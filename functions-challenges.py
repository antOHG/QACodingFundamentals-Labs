
#  functions challenges - created by AM 26/04/2023

# 1)	Password checker:
# Write a function that has a list with some common passwords as strings (stored as a variable) inside it. Have an input statement that asks the user for a password. If the input matches any string from the list print ‘Use a safer password {password} is compromised’, else print ‘password is safe’. 
# 2)	Simple calc:
# Write a function that takes 2 numbers as user input and then adds/subtracts/multiplies them and prints out the results. Eg; if user enters 10 and 5 the print-out should read ‘ sum is x, sub is y and multiply is z’.
# 3)	Write a function that takes 3 numbers as arguments, and returns the highest number.    
# 4)	Write a function that accepts a number as user input and returns whether the number is odd or even. 
# 5)	Write a function that converts a user inputted string into uppercase. 
# 6)	Write a function that accepts a radius and returns the area of a circle – search online for the correct equation to use. 
# 7)	Write a function that takes a temperature in degrees Celsius as user-input and converts to Fahrenheit.


class Solution(object):
   def strongPasswordChecker(self, s):
      missing_type = 3
      if any('a' <= c <= 'z' for c in s): missing_type -= 1
      if any('A' <= c <= 'Z' for c in s): missing_type -= 1
      if any(c.isdigit() for c in s): missing_type -= 1
      change = 0
      one = two = 0
      p = 2
      while p < len(s):
         if s[p] == s[p-1] == s[p-2]:
            length = 2
            while p < len(s) and s[p] == s[p-1]:
               length += 1
               p += 1
            change += length / 3
            if length % 3 == 0: one += 1
            elif length % 3 == 1: two += 1
         else:
            p += 1
      if len(s) < 6:
         return max(missing_type, 6 - len(s))
      elif len(s) <= 20:
         return max(missing_type, change)
      else:
         delete = len(s) - 20
         change -= min(delete, one)
         change -= min(max(delete - one, 0), two * 2) / 2
         change -= max(delete - one - 2 * two, 0) / 3
         return delete + max(missing_type, change)
ob = Solution()
print(ob.strongPasswordChecker('Acsds123'))