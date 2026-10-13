# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m, n = 0, 0
        # Compute m:
        curr = l1
        place = 1
        while curr != None:
            m += curr.val * (10 ** (place-1))
            place += 1
            curr = curr.next

        # Compute n:
        curr = l2
        place = 1
        while curr != None:
            n += curr.val * (10 ** (place-1))
            place += 1
            curr = curr.next
        print(m, n)
        # Compute sum
        s = m + n
        # 9 7 5
        # 5 -> 7 -> 9
        # Build linked list
        place = 1
        x = s
        print(s)
        head, prev = None, None
        if x == 0:
            return ListNode(0, None)
        while x != 0:
            #print(place)
            xprev = x
            x = (xprev // (10 ** place)) * (10 ** place)
            digit = (xprev - x) // (10 ** (place-1))
            print("Digit:",digit, "X:",x)
            node = ListNode(digit, None)
            if head == None:
                head = node
            if prev != None:
                prev.next = node
            prev = node
            place += 1
        return head

        



        