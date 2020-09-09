class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time and O(1) space
# two passes
def removeKthNodeFromEnd(head, k):
    length = 0
    current = head
    while current is not None:
        length += 1
        current = current.next
	if k == length:
        if head.next is None:
            return None
		head.value = head.next.value
		head.next = head.next.next
		return head
    counter = 1
    current = head
    while counter < (length - k):
        current = current.next
        counter += 1
    current.next = current.next.next
    return head


# O(n) time and O(1) space
# one pass
def removeKthNodeFromEnd(head, k):
    p1 = head
    p2 = head
    count = 0
    while count < k:
        p2 = p2.next
        count += 1
    if p2 is None:
        if head.next is None:
            return None
        head.value = head.next.value
        head.next = head.next.next
        return head
    while p2.next is not None:
        p2 = p2.next
        p1 = p1.next
    p1.next = p1.next.next
    return head


