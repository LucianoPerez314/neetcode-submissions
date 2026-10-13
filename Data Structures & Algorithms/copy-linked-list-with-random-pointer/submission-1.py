"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        # Store each node in a list
        llist = []
        random = {}
        idcs = {}
        curr = head
        i = 0
        while curr != None:
            llist.append(curr)
            random[curr] = curr.random
            idcs[curr] = i
            curr = curr.next
            i += 1
        copies = []
        # Make a copy for each node.
        for i, node in enumerate(llist):
            n = Node(node.val, None, None)
            copies.append(n)
        l = len(copies)
        # Wire each node
        for i, node in enumerate(copies):
            if i < l-1:
                node.next = copies[i+1]
            randnode = random[llist[i]]
            if randnode != None:
                ridx = idcs[randnode]
                node.random = copies[ridx]
        return copies[0]






