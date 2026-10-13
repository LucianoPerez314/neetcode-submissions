class LNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        

    def get(self, key: int) -> int:
        if self.head == None:
            return -1
        #print("Getting:", key)
        # Check head
        curr = self.head
        if curr.key == key:
            val = curr.val
            self.removeNode(curr)
            self.insert(key, val)
            return val
        curr = curr.nxt
        # Otherwise while curr node does not equal head, check it
        while curr != self.head:
            if curr.key == key:
                val = curr.val
                self.removeNode(curr)
                self.insert(key, val)
                return val
            curr = curr.nxt
        # If we looped back to head, return -1
        return -1


    def put(self, key: int, value: int) -> None:
        if self.head == None:
            self.insert(key, value)
            return
        # Check head
        curr = self.head
        if curr.key == key:
            curr.val = value
            # Head is already MRU, just update value
            return
        curr = curr.nxt
        # Otherwise while curr node does not equal head, check it
        while curr != self.head:
            if curr.key == key:
                curr.val = value
                # Move to front to mark as most recently used
                self.removeNode(curr)
                self.insert(key, value)
                return
            curr = curr.nxt

        # If we looped back to head, now we must insert the node.
        self.insert(key, value)
        

    def removeNode(self, node):
        if node == self.head:
            print("Removing Head")
            if self.size == 1:
                self.head = None
                self.size -= 1
                return
            else:
                self.head = self.head.nxt
        # Remove tail
        node.nxt.prev = node.prev
        node.prev.nxt = node.nxt
        node.prev = None
        node.nxt = None
        self.size -= 1

    def insert(self, key:int, value:int) -> None:
        if self.head == None and self.capacity != 0:
            node = LNode(key, value)
            self.head = node
            self.head.nxt = self.head
            self.head.prev = self.head
            self.size += 1
            return 
        #print("Head Before:", self.head)
        # If full size, evict LRU
        if self.size == self.capacity:
            self.removeNode(self.head.prev)

        # After removal, check if head became None (capacity = 1 case)
        if self.head == None:
            node = LNode(key, value)
            self.head = node
            self.head.nxt = self.head
            self.head.prev = self.head
            self.size += 1
            return
        # Insert node as between head and tail
        node = LNode(key, value)   
        tail = None    
        try:
            if self.head == None:
                print("Head After:", self.head)
            tail = self.head.prev
        except AttributeError as e:
            print("Caught error:", e)
            print("self.head is:", self.head)

        node.nxt = self.head
        node.prev = tail
        tail.nxt = node
        self.head.prev = node
        self.head = node
        self.size += 1



        
