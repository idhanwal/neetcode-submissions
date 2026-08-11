# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergell(l1, l2):
            dummy = ListNode(0)
            curr = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1:
                curr.next = l1
            else:
                curr.next = l2

            return dummy.next

        if len(lists) == 0:
            return None
        def divide(lists, l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]
            
            mid = (l + r) // 2

            left = divide(lists, l, mid)
            right = divide(lists, mid + 1, r)

            return mergell(left, right)
        
        return divide(lists, 0, len(lists) - 1)

            
