# brute force approach
# O(n^2) time and O(1) space
# n is length of array
def twoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i],array[j]]
    return []

# O(n) time and O(n) space
# n is length of array
def twoNumberSum(array,targetSum):
    differences = {}
    for num in array:
        current_difference = targetSum - num
        if current_difference in differences:
            return [current_difference,num]
        differences[num] = True
    return []