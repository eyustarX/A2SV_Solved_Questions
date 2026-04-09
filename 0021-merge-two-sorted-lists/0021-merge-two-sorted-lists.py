# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while list1:
            stack.append(list1.val)
            list1 = list1.next
        
        while list2:
            stack.append(list2.val)
            list2 = list2.next
        
        if not stack:
            return None

        stack.sort()
        head = ListNode(stack[0])
        curr = head

        for i in range(1, len(stack)):
            curr.next = ListNode(stack[i])
            curr = curr.next

        return head