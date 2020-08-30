class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time and O(d) space
# n is no.of nodes and d is depth of BST
def validateBst(tree):
    return validateBstHelper(tree,float("-inf"),float("inf"))

def validateBstHelper(node,min_value,max_value):
    if node is None:
        return True
    if node.value < min_value or node.value >= max_value:
        return False
    return validateBstHelper(node.left,min_value,node.value) and validateBstHelper(node.right,node.value,max_value)

