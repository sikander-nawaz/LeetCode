# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findKthNode(self, head, k):
        temp = head
        while k > 1:
            temp = temp.next
            k -= 1
        return temp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: Calculate length and find tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize rotations
        k %= length
        if k == 0:
            return head

        # Step 3: Form a circular linked list
        tail.next = head

        # Step 4: Find the new head and tail
        newTail = self.findKthNode(head, length - k)
        newHead = newTail.next
        newTail.next = None  # Break the circular link

        # Step 5: Return the new head
        return newHead