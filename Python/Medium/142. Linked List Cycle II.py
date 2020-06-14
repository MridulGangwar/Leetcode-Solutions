# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        try:
            lenCycle = self.lengthCycle(head)

            pt1, pt2 = head, head
            while lenCycle>0:
                pt2 = pt2.next
                lenCycle-=1
        
            while pt1!=pt2:
                pt1 = pt1.next
                pt2 = pt2.next
            return pt1
        except:
            return None
            
        
    def lengthCycle(self,head):
        slow, fast = head,head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return self.count(slow)
            
    def count(self,slow):
        length = 0
        temp = slow
        while True:
            length+=1
            temp=temp.next
            if temp==slow:
                return length 
				

## Solution 2

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        isCycle = self.identifyCycle(head)
        if not isCycle:
            return None
        
        stack = []
        while True:
            if head in stack:
                return head
            stack.append(head)
            head=head.next
            
    def identifyCycle(self,head):
        
        while head:
            if not head.val:
                return True
            head.val=None
            head = head.next
            
        return False
        