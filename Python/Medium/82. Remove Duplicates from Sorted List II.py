# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head
        
        while prev.next is not None:
            curr = prev.next
            while curr.next is not None and curr.val==curr.next.val:
                curr=curr.next
                
            if curr!=prev.next:
                prev.next=curr.next
            else:
                prev=prev.next
                
        return dummy.next