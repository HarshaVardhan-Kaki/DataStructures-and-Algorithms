# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time complexity for any case
# O(log(n)) stack space for recursive calls if tree is balanced, otherwise O(n)
# O(n) space for output array because there can be atmost 1/2 children in binary tree
# so O(n) time and O(n) space
def branchSums(root):
    sums = []
    branchSumsHelper(root,0,sums)
    return sums

def branchSumsHelper(node,running_sum,sums):
    if node is None:
        return
    current_sum = running_sum + node.value
    if node.left is None and node.right is None:
        sums.append(current_sum)
    branchSumsHelper(node.left,current_sum,sums)
    branchSumsHelper(node.right,current_sum,sums)

