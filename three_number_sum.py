# O(n^2) time and O(n) space
# n is length of array
def threeNumberSum(array,target):
    triplets = []
    array.sort()
    for i in range(len(array)):
        left = i + 1
        right = len(array)-1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target:
                triplets.append([array[i],array[left],array[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return triplets

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],0))