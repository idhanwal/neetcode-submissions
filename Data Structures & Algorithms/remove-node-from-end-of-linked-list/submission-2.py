# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        
        pos = size - n

        node = head
        while node and pos > 0:
            pos -= 1
            node = node.next
        
        nextNode = node.next
        prev = head
        if prev == node:
            head = head.next
            return head
        
        while prev.next != node:
            prev = prev.next
        
        prev.next = nextNode

        return head
        
        