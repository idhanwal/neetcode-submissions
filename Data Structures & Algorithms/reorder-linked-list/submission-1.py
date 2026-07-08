# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def get_length(head):
            node = head
            count = 0
            while node is not None:
                print(node.val)
                count += 1
                node = node.next
            return count
        
        def print_ll(head):
            node = head
            res = []
            while node is not None:
                res.append(node.val)
                node = node.next
            print(res)


        def reverse_ll(head):
            curr = head
            prev = None
            next = None
            while curr is not None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        
        length = get_length(head)
        cut =  int(length/2) if length%2==0 else int(length/2) + 1
        second_head = head
        last1 = None
        while cut > 0:
            last1 = second_head
            second_head = second_head.next
            cut -= 1
        last1.next = None
        second_head = reverse_ll(second_head)
        node = head
        # print_ll(head)
        # print_ll(second_head)
        while node is not None and second_head is not None:
            middle = second_head
            second_head = second_head.next
            next = node.next
            node.next = middle
            middle.next = next
            node = node.next.next
        

