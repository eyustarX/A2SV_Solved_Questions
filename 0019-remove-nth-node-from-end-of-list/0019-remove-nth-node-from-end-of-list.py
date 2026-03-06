# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        right = dummy
        left = dummy
        count = 0

        while right:
            if count <= n:
                right = right.next
            
            else:
                right = right.next
                left = left.next
            
            count += 1
        
        # if not left:
        #     return head.next
        
        left.next = left.next.next
        print(left.val)
        return dummy.next