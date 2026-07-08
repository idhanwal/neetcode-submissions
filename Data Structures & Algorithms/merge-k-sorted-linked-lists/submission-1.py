# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergell(l1, l2):
            if not l1 and not l2:
                return None
            if not l1:
                return l2
            if not l2:
                return l1

            if l1.val < l2.val:
                l1.next = mergell(l1.next, l2)
                return l1
            else:
                l2.next = mergell(l1, l2.next)
                return l2
        
        res = None
        for ll in lists:
            res = mergell(ll, res)
        
        return res

            
