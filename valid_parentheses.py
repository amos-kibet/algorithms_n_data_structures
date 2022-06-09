"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(]"
Output: false

Example 3:
Input: s = "()[]{}"
Output: true
"""

class Solution:

  # Solution 1:
    # def isValid(s):

    #   OPENING = '('
    #   stack = []

    #   for ss in s:
    #     if ss == OPENING:
    #       stack.append(ss)
    #     else:
    #       try:
    #         stack.pop()
    #       except IndexError: # too many closing parentheses
    #         return False
    #   return len(stack) == 0 # false if too many opening parentheses

    # #print(isValid('((()))')) # => True
    # print(isValid('(()'))  # => False
    # #print(isValid('())'))  # => False

    # Solution 2:
    # def isValid(s):
    #   if len(s) != 0:
    #     return False

    #   opening = "{[("
    #   closing = "}])"
    #   brackets = {')': '(', '}': '{', ']': '['}
    #   stack = []

    #   for char in s:
    #       if char in opening:
    #           stack.append(char)
    #       elif char in closing:
    #           if len(stack) == 0:
    #               return False
    #           if stack[-1] == brackets[char]:
    #               stack.pop()
    #           else:
    #               return False
    #   return len(stack) == 0

    # print(isValid('((()))'))
    # print(isValid('([{[]})'))


    # Solution 3:
    # def isValid(s):
    #   if len(s) % 2 != 0:
    #       return False
    #   dict = {'(' : ')', '[' : ']', '{' : '}'}
    #   stack = []
    #   for i in s:
    #     if i in dict.keys():
    #       stack.append(i)
    #     else:
    #       if stack == []:
    #         return False
    #       a = stack.pop()
    #       if i!= dict[a]:
    #         return False
    #   return stack == []

    # print(isValid('((()))'))
    # #print(isValid('([{[]})'))
