# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length(head):
            count = 0
            node = head
            while node is not None:
                count += 1
                node = node.next
            return count
        
        length = get_length(head)

        node = ListNode(0)
        node.next = head
        start = node
        pos = 0
        while start is not None and pos < length - n:
            pos += 1
            start = start.next
        print(start.val)
        skip = start.next.next
        start.next = skip
        return node.next
        