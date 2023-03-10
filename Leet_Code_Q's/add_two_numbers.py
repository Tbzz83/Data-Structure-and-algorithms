# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        tail = res

        while l1 or l2 or carry:
            firstNum = l1.val if l1 else 0
            secondNum = l2.val if l2 else 0
            sum = firstNum + secondNum + carry
            num = sum % 10 # This is the number we want for tail.next.
            # Returning sum % 10 will give us the num in the 1's position. (Eg, 15 % 10 = 5)
            carry = sum // 10 # The '1' gets updated to the carry variable since for example 15 // 10 = 1.
            tail.next = ListNode(num)

            tail = tail.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        return res.next
