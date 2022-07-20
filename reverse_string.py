"""
Write a function that reverses a string. The input string is given as an array of characters s. 
You must do this by modifying the input array in-place with 0(1) extra memory.

Example 1:
Input: s = ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]

Constraints:
  1. 1 <= s.length <= 10^5
  2. s[i] is a printable ascii character
"""


class Solution:
    def reverse_string(s):
        """
        Do not return anything, modify s in-place instead.
        """

        # My first naive solution, swapping in-place: O(n) time & O(1) space
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

        # Using a stack: O(n) time & O(n) space. Works but does not meet requirements.
        # stack = []
        # for c in s:
        #     stack.append(c)

        # i = 0
        # while stack:
        #     s[i] = stack.pop()
        #     i += 1

        # Using recursion: O(n) time & O(n) space. Works but does not meet requirements.
        # def reverse(l, r):
        #     if l < r:
        #         s[l], s[r] = s[r], s[l]
        #         reverse(l+1, r-1)
        # reverse(0, len(s)-1)

        # Insanely short solution:
        # s.reverse()

    print(reverse_string(["h", "e", "l", "l", "o"]))
