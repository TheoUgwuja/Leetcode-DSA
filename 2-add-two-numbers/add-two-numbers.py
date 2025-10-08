# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy head to simplify list construction
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10  # Compute carry for next iteration
            digit = total % 10   # Current digit

            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        #linked list are not empty
        #the digits are backwards not ordered so if the real number is 752 the list verstion is 257
        #wants me to take the list numbers out backwards first using some kind of -1 indexing
        #then put it into a variable lets say FL1 FL2 (f standing for fixed) add FL1 + FL2 then
        #put it in a list again backwards first 