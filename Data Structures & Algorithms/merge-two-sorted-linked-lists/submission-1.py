# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        if list1.val <= list2.val:
            baseList, otherList = list1, list2
            node1, next1, node2 = list1, list1.next, list2
        else:
            baseList, otherList = list2, list1
            node1, next1, node2 = list2, list2.next, list1

        while node2 != None:
            if next1 == None:
                node1.next = node2
                break
            elif node1.val <= node2.val and node2.val <= next1.val:
                print("Before",node1.val, next1.val, node2.val)
                temp = node2.next
                node1.next = node2
                node2.next = next1
                node2 = temp
                node1 = node1.next
                next1 = node1.next
            else:
                print("Before", node1.val, next1.val, node2.val)
                node1 = node1.next
                next1 = next1.next
        return baseList

                



