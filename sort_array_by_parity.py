class Solution:
    def sortArrayByParity(nums):
        # new_nums = []
        # for i in range(len(nums) - 1):
        #     if nums[i] % 2 == 0:
        #         new_nums.append(nums[i])
        # for j in range(len(nums)):
        #     while nums[i] not in new_nums:
        #         new_nums.append(nums[i])
        # return new_nums

        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 0:
                l += 1
            while l < r and nums[r] % 2 == 1:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return nums

    sortArrayByParity([1, 2, 3, 5])
