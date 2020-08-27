class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# O(log(n)) time and O(1) space - if tree is balanced
# O(n) time and O(1) space - worst case
def findClosestValueInBst(tree, target):
    closest = float("inf")
    node = tree
    while node is not None:
        if node.value == target:
            return node.value
        if abs(target - node.value) < abs(target - closest):
            closest = node.value
        if target < node.value:
            node = node.left
        elif target > node.value:
            node = node.right
        else:
            break
    return closest

# recursive approach
# O(log(n)) time and O(log(n)) space - if tree is balanced
# O(n) time and O(n) space - worst case
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree,target,float("inf"))

def findClosestValueInBstHelper(node,target,closest):
    if node is None:
        return closest
    if abs(target - node.value) < abs(target - closest):
        closest = node.value
    if target < node.value:
        return findClosestValueInBstHelper(node.left,target,closest)
    elif target > node.value:
        return findClosestValueInBstHelper(node.right,target,closest)
    else:
        return closest
