class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) > 0:
            temp = nums[0]
            i = 1
        else:
            return(len(nums))
#         time here is o(n)
        while i < len(nums):
            if nums[i] == temp:
                nums.pop(i)
            else:
                temp = nums[i]
                i += 1
                
#         storage would be o(n)-k
        return(len(nums))