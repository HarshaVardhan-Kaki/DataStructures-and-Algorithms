# O(nk) time and O(1) space
# n is length of array
class Solution:
    def rotate(self, nums,k):
        k = k % len(nums)
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j],previous = previous,nums[j]
        return nums

# O(n) time and O(n) space
# n is length of array
class Solution:
    def rotate(self, nums,k):
        k = k % len(nums)
        temp = [0 for num in nums]
        for i in range(len(nums)):
            temp[i+k] = nums[i]
        nums[:] = temp
        return nums

