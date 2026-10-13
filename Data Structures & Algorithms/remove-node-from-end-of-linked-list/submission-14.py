# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Distance anchor and lookahead
        anchor, lookahead = head, head
        i = n
        for _ in range(n - 1):
            lookahead = lookahead.next
        print(anchor.val, lookahead.val)
        # Step 2: Move lookahead to the end whilst dragging anchor
        prev = None
        while lookahead.next != None:
            prev = anchor
            anchor = anchor.next
            lookahead = lookahead.next
        print(head.val, anchor.val, lookahead.val)
        print(anchor == head)
        # Step 3: Remove anchor from the list.
        if prev != None:
            prev.next = anchor.next
        if anchor != head:
            return head
        print("HERE")
        print(head.next)
        if head.next != None:
            print("Yo", head.next.val)
        return head.next



            
        