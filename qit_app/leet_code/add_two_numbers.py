# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listNodeToInt(ln):
            o = ""
            x = ln
            while x is not None:
                o += str(x.val)
                x = x.next

            return int(o[::-1])

        def intToListNode(i):
            o = None
            for x in str(i):
                o = ListNode(int(x), o)

            return o

        return intToListNode(listNodeToInt(l1) + listNodeToInt(l2))
