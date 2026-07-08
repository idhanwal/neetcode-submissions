# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        curr1 = list1
        curr2 = list2
        head = None
        if curr1.val < curr2.val:
                head = curr1
                curr1 = curr1.next
                newCurr = head
        else:
            head = curr2
            newCurr = head
            curr2 = curr2.next
        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                newCurr.next = curr1
                curr1 = curr1.next
                newCurr = newCurr.next
            else:
                newCurr.next = curr2
                curr2 = curr2.next
                newCurr = newCurr.next
        
        while curr1 != None:
            newCurr.next = curr1
            curr1 = curr1.next 
            newCurr = newCurr.next

        while curr2 != None:
            newCurr.next = curr2
            curr2 = curr2.next
            newCurr = newCurr.next

        return head 