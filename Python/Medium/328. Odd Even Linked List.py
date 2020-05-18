# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        odd_head = ListNode(0)
        even_head = ListNode(0)
        odd_start = odd_head
        even_start = even_head
        is_odd = True
        
        while head:
            if is_odd:
                odd_head.next = head
                odd_head = odd_head.next
            else:
                even_head.next = head
                even_head = even_head.next
            is_odd = not is_odd
            head=head.next
            
        even_head.next=None
        odd_head.next = even_start.next
        
        return odd_start.next
            
        