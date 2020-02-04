class CircularQueue:
    def __init__(self, size):
        self._items = []
        self.size = size
        self.first = None
        self.last = None

    def isEmpty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def enqueue(self, item):
        assert not len(self) >= self.size, "Maximum size exceeded! Cannot enqueue more elements in to the queue."
        self._items.append(item)
        node = _CircularQueueNode(item)
        
        if self.isEmpty():
            self.first = node
            # self.last
            
        else:
            node.back = self.first
            node.front = self.last
            
            self.last.back = node

            # self.first.back = node
            # self.first.front = self.last
            # self.last.back = self.first
        # if self.last is not None:
        #     self.last.front
        
        self.last = node
        self.first.front = self.last
            # self.last.front = self.
            
            
        # self.last = node
        
        

    # def dequeue(self):
    #     assert not self.isEmpty(), "can not dequeue from an empty queue"
    #     node = self._qhead
    #     if self._qhead is self._qtail:
    #         self._qtail = None
    #     self._qhead = self._qhead.next
    #     self._count -= 1
    #     return node.item

    # def next(self):


class _CircularQueueNode:
    def __init__(self, item):
        self.item = item
        self.front = None
        self.back = None

cQ = CircularQueue(1)
cQ.enqueue(5)

print(cQ)
print(cQ.head)
print(cQ.tail)
        
        





    

