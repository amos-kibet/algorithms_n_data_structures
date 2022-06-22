#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.


from re import T
from matplotlib.pyplot import table
from regex import I


class Solution:
#     # Solution 1: Brute force solution
#     def two_sum(nums, target):
#         for i in range(len(nums)):
#           for j in range(i, len(nums)):
#             if nums[i] + nums[j] == target:
#               print([i, j])

#     two_sum([1,2,3,5], 5)

    # def two_sum_2(nums, target):
      
    #   print()

  # Solution 2
  # def two_sum_2(nums, target):
  #   values = {} #empty dictionary, to hold value:index pairs
  #   for idx, value in enumerate(nums):
  #     if target - value in values:
  #       return [values[target - value], idx]
  #     else:
  #       values[value] = idx

  # nums = [1,2,3,4,5]
  # target = 5
  # print(two_sum_2(nums, target))

  # Solution 3: Two pointers
  # def two_sum_3(nums, target):
  #   l, r = 0, len(nums) -1

    
  #   while l < r:
  #     current_sum = nums[l] + nums[r]
  #     if current_sum < target:
  #       l += 1
  #     elif current_sum > target:
  #       r -= 1
  #     else:
  #       return [l, r]

  # nums = [1,2,3,4,5]
  # target = 5
  # print(two_sum_3(nums, target))

  #Solution 4:
  # def two_sum_4(nums, target):
  #   values = {} #empty hash table, to hold index and values from list
  #   for i, num in enumerate(nums):
  #     diff = target - num
  #     if diff in values:
  #       return [i, values[diff]]
  #     values[num] = i
  #   return []

  # nums = [2,1,3,5,4]
  # target = 5
  # print(two_sum_4(nums, target))

  # Eddie's solution
  # def two_sum_5(nums, target):
  #   """
  #   :type nums: List[int]
  #   :type target: int
  #   :rtype: List[int]
  #   """
  #   for i in nums:
  #     y=target-i # complements of target
            
  #     if y in nums and nums.index(i)!=nums.index(y):
  #       return [nums.index(i),nums.index(y)]
  #     elif y in nums and nums.index(i)==nums.index(y):
  #       fake=nums.index(i)
  #       nums[nums.index(i)]="a"
  #       if y in nums:
  #         return [fake,nums.index(y)]
  #       else:
  #         continue
  #     else:
  #       print("lacking")

  # nums = [3,3,4,5,6]
  # target = 6
  # print(two_sum_5(nums, target))
  

  # Trial Solution
  def two_sum_5(nums, target):
    dict = {}
    for i in range(len(nums)-1):
      complement = target -nums[i]
      #print(complement)
      if complement in dict:
        return [dict[complement], i]
      dict[i] = complement
    return None

  nums = [3,3,4,5,6]
  target = 6
  print(two_sum_5(nums, target))
      