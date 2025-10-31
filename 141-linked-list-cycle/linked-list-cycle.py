# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1 step
            fast = fast.next.next     # Move fast pointer by 2 steps
            
            if slow == fast:          # If they meet, there’s a cycle
                return True
        
        return False                   # If fast reaches the end, no cycle
