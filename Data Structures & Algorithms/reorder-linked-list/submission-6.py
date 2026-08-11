# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeMap = {}
        curr = head
        i = 0
        while curr:
            nodeMap[i] = curr
            curr = curr.next
            i += 1
        length = i
        print(nodeMap)
        dummyNode = node = ListNode()
        l = 0
        r = length - 1
        while l <= r:
            if l == r:
                node.next = nodeMap[l]
                node = node.next
                node.next = None
            else:
                a = nodeMap[l]
                b = nodeMap[r]
                a.next = b
                node.next = a
                node = b
            l += 1
            r -= 1
        if l > r:
            node.next = None
        head = dummyNode.next
            





        




