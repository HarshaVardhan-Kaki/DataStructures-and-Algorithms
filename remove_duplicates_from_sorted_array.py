# leetcode

# O(n) time and O(1) space
# n is length of array
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        unique_elements = 1
        last_unique_idx = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[last_unique_idx]:
                continue
            else:
                nums[last_unique_idx+1] = nums[i]
                last_unique_idx +=1
                unique_elements += 1
        return unique_elements

# even though this solution returns correct length..we need to return array 
# that brings unique elements to the front
# class Solution:
#     def removeDuplicates(self, nums):
#         if len(nums) == 1:
#             return 1
#         unique_elements = 1
#         previous_seen = nums[0]
#         for i in range(1,len(nums)):
#             if nums[i] == previous_seen:
#                 continue
#             else:
#                 previous_seen = nums[i]
#                 unique_elements += 1
#         return unique_elements