# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_two_lists(one, two):
            res = ListNode()
            node = res
            while one != None and two != None:
                if one.val < two.val:
                    dummy = one
                    node.next = dummy
                    node = node.next
                    print(node.val)
                    one = one.next
                else:
                    dummy = two
                    node.next = dummy
                    node = node.next
                    print(node.val)
                    two = two.next
            if one:
                node.next = one
            if two:
                node.next = two
            return res.next
        
        def print_LL(head):
            node = head
            res = []
            while node != None:
                res.append(node.val)
                node = node.next
            print(res)

        if not lists:
            return 
        if len(lists) < 2:
            return lists[0]
        for i in range(1, len(lists)):
            ll1 = lists[0]
            ll2 = lists[i]
            lists[0] = merge_two_lists(ll1, ll2)
            print_LL(lists[0])
        
        return lists[0]
                
                
                

            
