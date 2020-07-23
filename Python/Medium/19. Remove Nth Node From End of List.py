#Two pass solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        l=0
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        node = dummy.next
        while node:
            l+=1
            node=node.next
            
        k = l-n
        
        currA = dummy
        while k:
            currA = currA.next
            k-=1
            
        currA.next = currA.next.next
        
        return dummy.next
		
#One pass solution		
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if not head:
            return head
        
        l=0
        
        dummy = ListNode(0)
        dummy.next = head
        pta,ptb = dummy.next, dummy
        
        while l!=n:
            l+=1
            pta=pta.next
        
        while pta:
            pta = pta.next
            ptb = ptb.next
        
        ptb.next = ptb.next.next
        
        return dummy.next