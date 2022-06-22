"""
Have the function 'string_challenge(str) take the str parameter being passed and determine if it is a valid serial number with the following constraints:
  1. It needs to contain three sets each with three digits (1 through to 9) separated by a period.
  2. The first set of digits must add up to an even number.
  3. The second set of digits must add up to an odd number.
  4. The last digit in each set must be larger than the two previous digits in the same set.

  Example 1:
  Input: "11.1244.667"
  Output: false

  Example 2:
  Input: "114.568.112"
  Output: true

If all of the conditions are met, the program should return true, otherwise false.
"""

def string_challenge(str):
  if len(str) == 11:
    if int(str[10]) > int(str[9]) and int(str[10]) > int(str[8]):
      if str[3] == ".":
        if (int(str[0] + str[1] + str[2])) % 2 == 0:
          if int(str[2]) > int(str[1]) and int(str[2]) > int(str[0]):
            if str[7] == ".":
              if (int(str[4] + str[5] + str[6])) % 2 == 0:
                if int(str[2]) > int(str[1]) and int(str[2]) > int(str[0]):
                  return True
  return False

  
print(string_challenge("114.568.112"))



