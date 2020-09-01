# O(n^2) time and O(n) space
# n is length of array
class Solution:
    def threeSum(self, array):
        array.sort()
        triplets = []
        for i in range(0,len(array)-2):
            if i != 0 and array[i] == array[i-1]:
                continue
            left = i + 1
            right = len(array) - 1
            while left < right:
                if left > i + 1 and array[left] == array[left - 1]:
                    left += 1
                    continue
                current_sum = array[i] + array[left] + array[right]
                if current_sum == 0:
                    triplets.append([array[i],array[left],array[right]])
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
        return triplets

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
