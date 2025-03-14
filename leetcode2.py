# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value = l1.val + l2.val
        add = value // 10
        val = value % 10
        node = root = ListNode(val=val)

        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            l2_val = l2.val if l2 is not None else 0
            l1_val = l1.val if l1 is not None else 0
            value = l2_val + l1_val + add

            add = value // 10
            val = value % 10
            print(val)
            new_node = ListNode(val=val)
            node.next = new_node

            node = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if not (l1 or l2):
                break

        if add:
            new_node = ListNode(val=add)
            node.next = new_node

        return root