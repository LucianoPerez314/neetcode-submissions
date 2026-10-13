# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Determine length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        # 2. Split list
        hidx = (length + 1) // 2
        idx = 0
        prev = None
        curr = head

        while curr:
            if idx == hidx:
                prev.next = None   # CUT
                halfway = curr
                break
            prev = curr
            curr = curr.next
            idx += 1

        # 3. Reverse second half
        rcurr = rev(halfway)

        # 4. Merge
        curr = head
        while curr and rcurr:
            nnext = curr.next
            rnext = rcurr.next

            curr.next = rcurr
            rcurr.next = nnext

            curr = nnext
            rcurr = rnext







def rev(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    l = head
    m = head.next
    head.next = None

    while m:
        r = m.next
        m.next = l
        l = m
        m = r

    return l

        