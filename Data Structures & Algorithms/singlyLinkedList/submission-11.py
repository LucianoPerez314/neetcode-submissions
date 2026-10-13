class LinkedList:
    
    def __init__(self):
        self.Head = None
    
    def get(self, index: int) -> int:
        if self.Head == None:
                return -1
        # find node
        curr = self.Head
        for i in range(index):
            curr = curr.Next
            if curr == None:
                return -1
        # return value.
        if curr == None:
                return -1
        return curr.Value

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        old_head = self.Head
        new_head.Next = old_head
        self.Head = new_head
        print(self.getValues())

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        if self.Head == None:
            self.Head = new_tail
            return 
        curr = self.Head
        while curr.Next != None:
            curr = curr.Next
        curr.Next = new_tail
        
    def remove(self, index: int) -> bool:
        if self.Head == None:
            return False
        elif index == 0:
            self.Head = self.Head.Next
            return True
        prev, curr = None, self.Head
        for i in range(index):
            prev = curr
            curr = curr.Next
            if curr == None:
                return False
                
        if curr == None:
                return False
        
        # remove found node.
        prev.Next = curr.Next
        curr.Next = None
        return True
        
    def getValues(self) -> List[int]:
        res = []
        curr = self.Head
        while curr != None:
            res.append(curr.Value)
            curr = curr.Next
        return res
        
class ListNode:

    def __init__(self, val):
        self.Value = val
        self.Next = None