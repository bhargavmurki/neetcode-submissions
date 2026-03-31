# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:
            kth = self.getkth(grpPrev, k)
            if not kth:
                break
            grpNext = kth.next

            prev, cur = kth.next, grpPrev.next
            while cur != grpNext:
                t = cur.next
                cur.next = prev
                prev = cur
                cur = t
            
            t = grpPrev.next
            grpPrev.next = kth
            grpPrev = t
        return dummy.next
        
    
    def getkth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr