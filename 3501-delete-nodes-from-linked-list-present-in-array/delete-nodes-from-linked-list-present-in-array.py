# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        h = {}
        for i in nums:
            h[i] = 1
        temp = head
        newhead = ListNode(-1)
        temp2 = newhead
        
        while temp is not None:
            if h.get(temp.val, None):
                temp = temp.next
            else:
                temp2.next = temp
                temp2 = temp
                temp = temp.next
        
        temp2.next = None
        return newhead.next
        