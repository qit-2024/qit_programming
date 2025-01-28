from .add_two_numbers_recursion import ListNode


def list_node_to_int(ln):
    o = ""
    x = ln
    while x is not None:
        o += str(x.val)
        x = x.next

    return int(o)


def int_to_list_node(i):
    o = None
    for x in str(i)[::-1]:
        o = ListNode(int(x), o)

    return o
