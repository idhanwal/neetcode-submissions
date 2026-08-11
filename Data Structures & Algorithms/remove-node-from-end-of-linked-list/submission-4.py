# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # size = 0
        # node = head
        # while node:
        #     size += 1
        #     node = node.next
        
        # pos = size - n

        # node = head
        # while node and pos > 0:
        #     pos -= 1
        #     node = node.next
        
        # nextNode = node.next
        # prev = head
        # if prev == node:
        #     head = head.next
        #     return head
        
        # while prev.next != node:
        #     prev = prev.next
        
        # prev.next = nextNode

        # return head
        
        nodeMap = {}
        i = 1
        curr = head
        while curr:
            nodeMap[i] = curr
            i += 1
            curr = curr.next
        
        size = i

        eliminate = size - n
        if eliminate == 1:
            return head.next
        if eliminate + 1 in nodeMap:
            nodeMap[eliminate - 1].next = nodeMap[eliminate + 1]
        else:
            nodeMap[eliminate - 1].next = None
        return head


        
