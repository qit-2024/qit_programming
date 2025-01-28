# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def add_two_numbers(l1, l2):

        def add_lists(x, y, c=0):
            z = x.val + y.val + c
            c = z // 10
            z = z % 10

            x = x.next
            y = y.next
            if (x is None) and (y is not None):
                if c > 0:
                    x = ListNode(0, None)
                else:

                    return ListNode(z, y)

            elif (x is not None) and (y is None):
                if c > 0:
                    y = ListNode(0, None)
                else:

                    return ListNode(z, x)

            elif (x is None) and (y is None):

                return ListNode(z, ListNode(c, None)) if c > 0 else ListNode(z, None)

            return ListNode(z, add_lists(x, y, c))

        return add_lists(l1, l2)
