# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def get_length(head):
            curr = head
            count = 0
            while curr:
                count += 1
                curr = curr.next
            return count
        length = get_length(head)
        print(length)
        def cut_ll(head, index):
            curr = head
            while curr and index >= 0:
                curr = curr.next
                index -= 1
            return head, curr
        h1, h2 = cut_ll(head, length//2)
        # print(h1.val, h2.val)
        node = h1
        while node.next != h2:
            node = node.next
        node.next = None
        # node = h1
        # n1 = []
        # while node:
        #     n1.append(node.val)
        #     node = node.next
        # print(n1)
        # node = h2
        # n2 = []
        # while node:
        #     n2.append(node.val)
        #     node = node.next
        # print(n2)
        def reversell(head):
            curr, next, prev = head, None, None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        
        h2 = reversell(h2)
        # node = h2
        # n2 = []
        # while node:
        #     n2.append(node.val)
        #     node = node.next
        # print(n2)
        def mergell(h1, h2, pick):
            if not h1 and not h2:
                return
            if not h1:
                return h2
            if not h2:
                return h1
            if pick:
                h1.next = mergell(h1.next, h2, False)
                return h1
            else:
                h2.next = mergell(h1, h2.next, True)
                return h2

        mergell(h1, h2, True)
        # n2 = []
        # while node:
        #     n2.append(node.val)
        #     node = node.next
        # print(n2)



