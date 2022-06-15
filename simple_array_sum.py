"""
Given an array of integers, find the sum of its elements.

For example, if the array ar=[1,2,3,], 1+2+3 = 6, so return 6
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    count = 0
    for i in range(len(ar)):
      if type(ar[i]) != int:
        return "Error: Some array values are not integer type!"
      count += ar[i]
    return count

print(simpleArraySum([1,2,3,4,'a',5]))