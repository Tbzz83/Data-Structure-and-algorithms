# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A_set = set()
        tailA = headA
        tailB = headB

        while tailA:
            A_set.add(tailA)
            tailA = tailA.next

        while tailB:
            if tailB in A_set:
                return tailB
            else:
                tailB = tailB.next
        return None

        print(A_set)



