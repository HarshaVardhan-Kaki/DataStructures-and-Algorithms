# leetcode

# O(n) time and O(1) space
# n is length of array
class Solution:
    def moveZeroes(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        while count < len(nums):
            nums[count] = 0
            count += 1
        

s = Solution()
s.moveZeroes([0,1,0,3,12])


        