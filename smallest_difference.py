# O(nlog(n)) + O(mlog(m)) time and O(1) space
# n is length of arrayOne and m is length of arrayTwo
def smallestDifference(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    p1 = 0
    p2 = 0
    smallest_difference = float("inf")
    result = []
    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        current_diff = abs(arrayOne[p1] - arrayTwo[p2])
        if current_diff < smallest_difference:
            result = [arrayOne[p1],arrayTwo[p2]]
            smallest_difference = current_diff
        if arrayOne[p1] < arrayTwo[p2]:
            p1 += 1
        elif arrayOne[p1] > arrayTwo[p2]:
            p2 += 1
        else:
            break
    return result

print(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]))

