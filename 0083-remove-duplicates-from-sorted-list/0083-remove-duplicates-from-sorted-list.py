# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy = prev = head
        dummy = dummy.next
        while dummy:
            if prev.val == dummy.val:
                prev.next = dummy.next
            else:
                prev = dummy
            dummy = dummy.next
        return head


            
