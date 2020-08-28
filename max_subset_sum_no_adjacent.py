# O(n) time and O(1) space
# n is length of array
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return max(array[0],array[1])
    nonadjacent_sum = array[0]
    adjacent_sum = max(array[1],array[0])
    for i in range(2,len(array)):
        current_max = max(adjacent_sum,array[i]+nonadjacent_sum)
        nonadjacent_sum = adjacent_sum
        adjacent_sum = current_max
    return adjacent_sum

# O(n) time and O(n) space
# n is length of array
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    non_adjacent_sums = [None for num in array]
    non_adjacent_sums[0] = array[0]
    non_adjacent_sums[1] = max(array[0],array[1])
    for i in range(2,len(array)):
        non_adjacent_sums[i] = max(non_adjacent_sums[i-1],array[i]+non_adjacent_sums[i-2])
    return non_adjacent_sums[-1]

